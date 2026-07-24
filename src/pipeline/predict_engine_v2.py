"""
predict_engine_v2.py

Purpose:
Execute the complete Version 2 generalized prediction pipeline
for Remaining Useful Life estimation.
"""

import logging
import os
from pathlib import Path

import numpy as np
import joblib
import pandas as pd
import torch

from backend.app.services.prediction_service import (
    save_prediction,
)

from backend.app.services.version2_service import (
    MODEL,
    predict_with_uncertainty,
)

from src.version2.generalized_decision_engine import (
    generate_decision,
)

# (We'll replace this import with the proper wrapper
# after we create it.)
from src.version2.explain_generalized_model import generate_attributions


logger = logging.getLogger(__name__)

ROOT_DIR = Path(__file__).resolve().parents[2]

GLOBAL_SCALER_PATH = (
    ROOT_DIR
    / "DATA"
    / "version2"
    / "models"
    / "global_scaler.pkl"
)

SEQUENCE_LENGTH = 40

EXPECTED_COLUMNS = 26


EXPECTED_COLUMN_NAMES = [
    "engine_id",
    "cycle",
    "op_setting_1",
    "op_setting_2",
    "op_setting_3",
    *[f"sensor_{i}" for i in range(1, 22)],
]


def validate_dataset(df, is_csv=True):
    """
    Validate uploaded dataset.
    """

    logger.info("Validating uploaded dataset.")

    if df.empty:
        logger.error("Validation failed: Uploaded dataset is empty.")
        raise ValueError("Uploaded dataset is empty.")

    if df.shape[1] != EXPECTED_COLUMNS:
        raise ValueError(
            f"Expected {EXPECTED_COLUMNS} columns but found {df.shape[1]}."
        )


    # Validate column names only for CSV uploads

    if is_csv:

        if list(df.columns) != EXPECTED_COLUMN_NAMES:

            raise ValueError(
            "Invalid dataset schema. Column names do not match the NASA C-MAPSS format."
        )

    

    try:
        df = df.apply(pd.to_numeric)
    except Exception:
        raise ValueError("Dataset contains non-numeric values.")

    missing_values = df.isnull().sum().sum()

    if missing_values > 0:
        logger.error(
        f"Validation failed: Dataset contains {missing_values} missing values."
    )
        raise ValueError(
            f"Dataset contains {missing_values} missing values."
        )



    # ----------------------------------
    # Duplicate Row Validation
    # ----------------------------------

    duplicate_rows = df.duplicated().sum()

    if duplicate_rows > 0:

        logger.error(
        f"Validation failed: {duplicate_rows} duplicate rows detected."
    )

        raise ValueError(
        f"Dataset contains {duplicate_rows} duplicate row(s)."
    )









    # ----------------------------------
    # Engine ID Validation
    # ----------------------------------

    if df["engine_id"].isnull().any():

        raise ValueError(
        "Engine ID column contains missing values."
    )

    if not pd.api.types.is_numeric_dtype(df["engine_id"]):

        raise ValueError(
        "Engine ID must contain numeric values only."
    )

    if (df["engine_id"] <= 0).any():

        logger.error(
        "Validation failed: Engine IDs must be positive integers."
    )
        raise ValueError(
        "Engine IDs must be positive integers."
    )

    if (df["engine_id"] % 1 != 0).any():

        raise ValueError(
        "Engine IDs must be integers."
    )


    # ----------------------------------
    # Cycle Ordering Validation
    # ----------------------------------

    for engine_id, engine_data in df.groupby("engine_id"):

        if not engine_data["cycle"].is_monotonic_increasing:

            logger.error(
        f"Validation failed: Engine {engine_id} has unsorted cycle values."
    )

            raise ValueError(
            f"Engine {engine_id} contains unsorted cycle values."
        )





    # ----------------------------------
    # Duplicate Cycle Validation
    # ----------------------------------

    for engine_id, engine_data in df.groupby("engine_id"):

        duplicate_cycles = engine_data["cycle"].duplicated().sum()

        if duplicate_cycles > 0:

            raise ValueError(
            f"Engine {engine_id} contains {duplicate_cycles} duplicate cycle(s)."
        )





    # ----------------------------------
    # Cycle Value Validation
    # ----------------------------------

    if (df["cycle"] <= 0).any():

        raise ValueError(
        "Cycle values must be greater than zero."
    )

    if (df["cycle"] % 1 != 0).any():

        raise ValueError(
        "Cycle values must be integers."
    )


    logger.info("Dataset validation completed successfully.")

    return True







def split_by_engine(df):
    """
    Split uploaded dataset into individual engines.
    """

    logger.info("Splitting dataset by engine.")

    engines = {}

    engine_ids = df["engine_id"].unique()

    for engine_id in engine_ids:
        engines[engine_id] = df[
            df["engine_id"] == engine_id
        ].copy()

    logger.info(f"Detected {len(engines)} engine(s).")

    return engines






def extract_latest_sequence(engine_df):
    """
    Extract the latest sequence from one engine.
    """

    engine_id = engine_df["engine_id"].iloc[0]
    engine_df = engine_df.sort_values(
    by="cycle"
).reset_index(drop=True)

    logger.info(f"Processing Engine ID: {engine_id}")
    logger.info(f"Engine contains {len(engine_df)} cycle(s).")

    if len(engine_df) < SEQUENCE_LENGTH:

        logger.info(
            f"Engine has fewer than {SEQUENCE_LENGTH} cycles. Applying padding."
        )

        padding_rows = SEQUENCE_LENGTH - len(engine_df)

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
            SEQUENCE_LENGTH
        ).reset_index(drop=True)


    logger.info(
    latest_sequence[["cycle"]].head(10)
)

    logger.info(
    latest_sequence[["cycle"]].tail(10)
)

    return latest_sequence








def preprocess_sequence(sequence):
    """
    Apply Version 2 preprocessing to one engine sequence.
    """

    processed = sequence.copy()

    feature_columns = [
        column
        for column in processed.columns
        if column not in [
            "engine_id",
            "cycle",
            "max_cycle",
            "RUL",
            "RUL_CLIPPED"
        ]
    ]

    scaler = joblib.load(GLOBAL_SCALER_PATH)

    logger.info("Global scaler loaded successfully.")


    logger.info(feature_columns)
    processed = scaler.transform(
        processed[feature_columns]
    )

    processed = torch.tensor(
        processed,
        dtype=torch.float32
    ).unsqueeze(0)

    return processed









def run_prediction_v2(csv_path: str) -> dict:
    """
    Run the complete Version 2 prediction pipeline.
    """

    logger.info(f"Starting Version 2 prediction for: {csv_path}")

    extension = os.path.splitext(csv_path)[1].lower()

    if extension == ".csv":

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
        header=None,
        names=column_names,
    )

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
            "Unsupported file format. Please upload a CSV or TXT file."
        )

    logger.info("Dataset loaded successfully.")

    # Validate uploaded dataset
    validate_dataset(
    df,
    is_csv=(extension == ".csv")
)

    # Split into individual engines
    engines = split_by_engine(df)

    predictions = []

    for engine_df in engines.values():

        engine_id = int(
        engine_df["engine_id"].iloc[0]
    )

        # Extract the latest sequence
        sequence = extract_latest_sequence(engine_df)

        # Apply Version 2 preprocessing
        processed_sequence = preprocess_sequence(sequence)
    

        logger.info(f"Processed sequence shape: {processed_sequence.shape}")


        logger.info("Input sequence preprocessed successfully.")


        # Predict RUL with uncertainty
        prediction_result = predict_with_uncertainty(
        processed_sequence.squeeze(0).numpy()
    )

        logger.info(
        f"Predicted RUL: {prediction_result['predicted_rul']}"
)

        logger.info(
        f"Uncertainty: {prediction_result['uncertainty']}"
)

        predicted_rul = min(
    125.0,
    max(
        0.0,
        round(prediction_result["predicted_rul"], 2)
    )
)

        uncertainty_std = prediction_result["uncertainty"]

        decision = prediction_result["decision"]

        logger.info(
        f"Prediction completed. RUL: {predicted_rul:.2f}"
    )



        # Generate Integrated Gradients feature importance
        feature_importance = generate_attributions(
        MODEL,
        processed_sequence
    )

        logger.info("Feature importance generated successfully.")

    

        # Calculate health score
        health_score = min(
        round((predicted_rul / 125) * 100),
        100
    )

        # Determine risk level
        if predicted_rul <= 15:
            risk = "Critical"
        elif predicted_rul <= 40:
            risk = "High"
        elif predicted_rul <= 80:
            risk = "Medium"
        else:
            risk = "Low"

        # Calculate confidence
        if uncertainty_std < 1:
            confidence = 98
        elif uncertainty_std < 2:
            confidence = 95
        elif uncertainty_std < 3:
            confidence = 90
        elif uncertainty_std < 5:
            confidence = 80
        else:
            confidence = 70

        logger.info(
        f"Risk: {risk}, Confidence: {confidence}%"
    )



        response = {

        "engine_id": engine_id,

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

        "uncertainty": uncertainty_std,

        "mc_samples": prediction_result["mc_samples"],

        "mc_mean": predicted_rul
        }

        predictions.append(response)

        save_prediction(response)


    

    logger.info("Prediction pipeline completed successfully.")

    return {
    "total_engines": len(predictions),
    "predictions": predictions
}