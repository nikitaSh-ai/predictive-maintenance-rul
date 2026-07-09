"""
predict_engine.py

Purpose:
Execute the complete prediction pipeline
for a new engine dataset.
"""


import joblib
import torch
from pathlib import Path
import pandas as pd
import os

from backend.app.services.model_service import model


ROOT_DIR = Path(__file__).resolve().parents[2]

SCALER_PATH = ROOT_DIR / "models" / "scaler.pkl"

def validate_dataset(df):
    """
    Validate uploaded dataset.
    """

    print("\nValidating Dataset...")

    if df.empty:

        raise ValueError(
            "Uploaded dataset is empty."
        )

    print("Dataset is not empty.")

    expected_columns = 26

    if df.shape[1] != expected_columns:

      raise ValueError(
        f"Expected {expected_columns} columns but found {df.shape[1]}."
     )

    print("Column count is valid.")


    try:

      df = df.apply(pd.to_numeric)

      print("All values are numeric.")

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

    print("No missing values found.")

    return True







def split_by_engine(df):
    """
    Split the uploaded dataset
    into individual engines.
    """

    print("\nSplitting Dataset by Engine...")

    engines = {}

    engine_ids = df.iloc[:, 0].unique()

    for engine_id in engine_ids:

        engine_df = df[
            df.iloc[:, 0] == engine_id
        ].copy()

        engines[engine_id] = engine_df

    print(f"Number of Engines : {len(engines)}")

    return engines









def extract_latest_sequence(
    engine_df,
    sequence_length=40
):
    """
    Extract the latest sequence
    from one engine.
    """

    print(
        f"\nEngine {engine_df.iloc[0,0]}"
    )

    print(
        f"Cycles : {len(engine_df)}"
    )

    if len(engine_df) < sequence_length:

        return None

    latest_sequence = engine_df.tail(
        sequence_length
    )

    print(
        "Latest Sequence Shape :",
        latest_sequence.shape
    )

    return latest_sequence



def preprocess_sequence(sequence):
    """
    Apply the same preprocessing
    used during training.
    """

    processed = sequence.copy()

    # Remove Engine ID
    processed = processed.drop(
    columns=[0]
    )

    # Remove Cycle
    processed = processed.drop(
    columns=[1]
    )

    print("\nAfter Removing ID & Cycle")

    print(processed.shape)

    # Remove constant features
    processed = processed.drop(
        columns=[2, 3, 7, 12, 18, 20, 21]
    )

    print("\nAfter Removing Constant Features")
    print(processed.shape)

    print("\nRemaining Columns")

    print(processed.columns.tolist())


    scaler = joblib.load(SCALER_PATH)

    print("\nScaler Loaded Successfully.")

    processed = scaler.transform(processed)

    print("\nAfter Scaling")
    print(processed.shape)

    processed = torch.tensor(
    processed,
    dtype=torch.float32
    )

    processed = processed.unsqueeze(0)

    print("\nTensor Shape")
    print(processed.shape)

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

    print("=" * 60)
    print("PREDICTION PIPELINE")
    print("=" * 60)

    print("\nInput File")
    print(csv_path)

    # -------------------------
    # Load Uploaded CSV
    # -------------------------

 

    extension = os.path.splitext(csv_path)[1].lower()

    if extension == ".csv":

      df = pd.read_csv(csv_path)

    elif extension == ".txt":

     df = pd.read_csv(
        csv_path,
        sep=r"\s+",
        header=None
      )

    else:

      raise ValueError(
        "Unsupported file format."
       )

    print("\nDataset Loaded Successfully.")
 
    print(df.head())

    print("\nDataset Shape")

    print(df.shape)

    validate_dataset(df)

    engines = split_by_engine(df)

    print("\nEngine IDs")

    print(list(engines.keys())[:10])


    first_engine = engines[1]

    sequence = extract_latest_sequence(
    first_engine
    )

    processed_sequence = preprocess_sequence(
    sequence
)
    
    model.eval()

    with torch.no_grad():
       prediction = model(processed_sequence)

    print("\nRaw Prediction")
    print(prediction)


    predicted_rul = round(prediction.item(), 2)

    print("\nPredicted RUL")
    print(predicted_rul)


    health_score = min(
    round((predicted_rul / 125) * 100),
    100
    )

    print("\nHealth Score")
    print(health_score)


    if predicted_rul <= 15:
      risk = "Critical"

    elif predicted_rul <= 40:
      risk = "High"

    elif predicted_rul <= 80:
      risk = "Medium"

    else:
      risk = "Low"

    print("\nRisk Level")
    print(risk)



    if risk == "Critical":
      recommendation = (
        "Immediate maintenance required."
    )

    elif risk == "High":
      recommendation = (
        "Schedule maintenance as soon as possible."
    )

    elif risk == "Medium":
      recommendation = (
        "Plan maintenance in upcoming cycles."
    )

    else:
      recommendation = (
        "Continue normal operation."
    )

    print("\nRecommendation")
    print(recommendation)

    confidence = 95

    print("\nConfidence")
    print(f"{confidence}%")
    
    print("\nLatest Sequence Preview")

    print(sequence.head())

    print("\nSequence Shape")

    print(sequence.shape)

    print("\nProcessed Shape")

    print(processed_sequence.shape)

#     return {
#     "dataset_shape": df.shape,
#     "num_engines": len(engines),
#     "sequence_shape": (
#         sequence.shape
#         if sequence is not None
#         else None
#     )
#    }


    return {

    "rul": predicted_rul,

    "risk": risk,

    "confidence": f"{confidence}%",

    "healthScore": health_score,

    "recommendation": recommendation,

    "inspection": (
        "Inspect immediately"
        if risk == "Critical"
        else
        "Inspect within 10 cycles"
        if risk == "High"
        else
        "Inspect within 30 cycles"
        if risk == "Medium"
        else
        "Routine inspection"
    ),

    "focus": (
        "Immediate maintenance"
        if risk == "Critical"
        else
        "Monitor degradation"
        if risk == "High"
        else
        "Routine monitoring"
    ),

    "summary": (
        f"Predicted Remaining Useful Life is {predicted_rul} cycles. "
        f"Current engine risk is {risk}. "
        f"{recommendation}"
    )

}

if __name__ == "__main__":

    run_prediction(
        "DATA/raw/train_FD001.txt"
    )