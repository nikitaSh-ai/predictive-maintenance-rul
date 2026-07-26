"""
predict_engine.py

Purpose:
Execute the complete prediction pipeline
for a new engine dataset.
"""





from backend.app.services.prediction_service import (
    save_prediction
)

from src.decision.decision_engine import (
    generate_decision
)

from src.explainability.uncertainty import (
    monte_carlo_prediction
)

from backend.app.services.explainability_service import generate_attributions
import joblib
import torch
from pathlib import Path
import pandas as pd
import os

from backend.app.services.model_service import model

import logging

logger = logging.getLogger(__name__)


ROOT_DIR = Path(__file__).resolve().parents[2]

SCALER_PATH = ROOT_DIR / "models" / "scaler.pkl"

def validate_dataset(df):
    """
    Validate uploaded dataset.
    """

    logger.info("Validating uploaded dataset.")

    if df.empty:

        raise ValueError(
            "Uploaded dataset is empty."
        )

    logger.info("Dataset validation passed: dataset is not empty.")

    expected_columns = 26

    if df.shape[1] != expected_columns:

      raise ValueError(
        f"Expected {expected_columns} columns but found {df.shape[1]}."
     )

    logger.info("Dataset validation passed: column count is valid.")


    try:

      df = df.apply(pd.to_numeric)

      logger.info("Dataset validation passed: all values are numeric.")

    except Exception:

      raise ValueError(
        "Dataset contains non-numeric values."
      )
    



    # -------------------------
    # Check Missing Values
    # -------------------------

    missing_values = df.isnull().sum().sum()

    if missing_values > 0:

      raise ValueError(
        f"Dataset contains {missing_values} missing values."
    )

    logger.info("Dataset validation passed: no missing values found.")

    return True







def split_by_engine(df):
    """
    Split the uploaded dataset
    into individual engines.
    """

    logger.info("Splitting dataset by engine.")

    engines = {}

    engine_ids = df.iloc[:, 0].unique()

    for engine_id in engine_ids:

        engine_df = df[
            df.iloc[:, 0] == engine_id
        ].copy()

        engines[engine_id] = engine_df

    logger.info(f"Detected {len(engines)} engine(s) in the uploaded dataset.")

    return engines









def extract_latest_sequence(
    engine_df,
    sequence_length=40
):
    """
    Extract the latest sequence
    from one engine.
    """

    logger.info(
    f"Processing Engine ID: {engine_df.iloc[0,0]}"
    )
    
    logger.info(
    f"Engine contains {len(engine_df)} cycle(s)."
    )

   

    if len(engine_df) < sequence_length:

      logger.info(
    "Engine sequence shorter than 40 cycles. Applying automatic padding."
     )

      padding_rows = sequence_length - len(engine_df)

      first_row = engine_df.iloc[[0]]

      padding = pd.concat(
        [first_row] * padding_rows,
        ignore_index=True
      )

      latest_sequence = pd.concat(
        [padding, engine_df],
        ignore_index=True
      )

    else:

      latest_sequence = engine_df.tail(
        sequence_length
      )

    return latest_sequence



def preprocess_sequence(sequence):
    """
    Apply the same preprocessing
    used during training.
    """

    processed = sequence.copy()

    # Remove Engine ID and Cycle
    processed = processed.drop(
     columns=[
        "engine_id",
        "cycle",
      ]
    )

    # Remove constant features
    processed = processed.drop(
    columns=[
        "op_setting_3",
        "sensor_1",
        "sensor_5",
        "sensor_10",
        "sensor_16",
        "sensor_18",
        "sensor_19",
      ]
    )

    
    


    scaler = joblib.load(SCALER_PATH)

    logger.info("Feature scaler loaded successfully.")

    processed = scaler.transform(processed)

    

    processed = torch.tensor(
    processed,
    dtype=torch.float32
    )

    processed = processed.unsqueeze(0)

    
    return processed

   





def run_prediction(csv_path):
    """
    Run the complete prediction pipeline.

    Parameters
    ----------
    csv_path : str
        Path of uploaded CSV file.

    Returns
    -------
    dict
        Prediction results.
    """

    logger.info(f"Starting prediction pipeline for file: {csv_path}")

    # -------------------------
    # Load Uploaded CSV
    # -------------------------

 

    extension = os.path.splitext(csv_path)[1].lower()

    if extension == ".csv":

      df = pd.read_csv(csv_path)

    elif extension == ".txt":

      column_names = [
        "engine_id",
        "cycle",
        "op_setting_1",
        "op_setting_2",
        "op_setting_3",
        *[f"sensor_{i}" for i in range(1, 22)],
      ]

      df = pd.read_csv(
        csv_path,
        sep=r"\s+",
        header=None,
        names=column_names,
      )

    else:

      raise ValueError(
        "Unsupported file format."
       )


    # ---------------------------------
    # Debug Logs
    # Remove or replace with logging
    # before deployment
    # ---------------------------------
    
    logger.info("Dataset loaded successfully.")
 
    

    

   

    validate_dataset(df)

    engines = split_by_engine(df)



    

    first_engine = next(iter(engines.values()))
   
    sequence = extract_latest_sequence(
    first_engine
    )

    processed_sequence = preprocess_sequence(
    sequence
)
    
    model.eval()

    with torch.no_grad():
      prediction = model(processed_sequence)

    logger.info("GRU model prediction completed.")


    feature_importance = generate_attributions(
     processed_sequence
    )

    

    


    uncertainty = monte_carlo_prediction(

    model,

    processed_sequence

   )

    

    


    predicted_rul = round(prediction.item(), 2)

    logger.info(f"Predicted RUL: {predicted_rul} cycles.")


    health_score = min(
    round((predicted_rul / 125) * 100),
    100
    )

    logger.info(f"Calculated Health Score: {health_score}%.")


    if predicted_rul <= 15:
      risk = "Critical"

    elif predicted_rul <= 40:
      risk = "High"

    elif predicted_rul <= 80:
      risk = "Medium"

    else:
      risk = "Low"

    logger.info(f"Risk Level: {risk}.")


    decision = generate_decision(
    risk,
    uncertainty["std"]
    )

    logger.info(
    f"Decision generated with priority {decision['priority']}."
    )


    

    if uncertainty["std"] < 1:

     confidence = 98

    elif uncertainty["std"] < 2:

     confidence = 95

    elif uncertainty["std"] < 3:

     confidence = 90

    elif uncertainty["std"] < 5:

     confidence = 80

    else:

     confidence = 70

    logger.info(
    f"Prediction confidence: {confidence}%."
    )
    
    logger.info(f"Columns: {list(df.columns)}")
    logger.info(f"Shape: {df.shape}")
    

    prediction_result = {

    "engine_id": int(first_engine["engine_id"].iloc[0]),

    "predicted_rul": predicted_rul,

    "risk": risk,

    "priority": decision["priority"],

    "confidence": f"{confidence}%",

    "health_score": health_score,


    "recommendation": decision["recommendation"],

    
    "inspection": decision["inspection"],


    "focus": decision["focus"],

    "reason": decision["reason"],

    "summary": (
        f"Predicted Remaining Useful Life is {predicted_rul} cycles. "
        f"Current engine risk is {risk}. "


       

        f"{decision['recommendation']}"
    ),

    "feature_importance": feature_importance, 

    "uncertainty": uncertainty["std"],

    "mc_mean": uncertainty["mean"],

    "mc_samples": uncertainty["samples"]

}
    save_prediction(prediction_result)
    return prediction_result

if __name__ == "__main__":

    run_prediction(
        "DATA/raw/train_FD001.txt"
    )