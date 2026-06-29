"""
scale_features.py

Purpose:
Scale numerical features using statistics from the
training dataset only.
"""

import os
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler


def scale_features():
    """
    Scale numerical features using the training dataset
    and save the scaler and scaled datasets.
    """

    # -----------------------
    # Load datasets
    # -----------------------
    train_df = pd.read_csv("DATA/processed/train_selected.csv")
    validation_df = pd.read_csv("DATA/processed/validation_selected.csv")
    test_df = pd.read_csv("DATA/processed/test_selected.csv")

    # -----------------------
    # Columns not to scale
    # -----------------------
    exclude_cols = [
        "engine_id",
        "cycle",
        "max_cycle",
        "RUL","RUL_CLIPPED"
    ]

    feature_cols = [
        col for col in train_df.columns
        if col not in exclude_cols
    ]

    print("=" * 60)
    print("FEATURE SCALING")
    print("=" * 60)

    print("\nNumber of Features:", len(feature_cols))

    # -----------------------
    # Fit scaler on train only
    # -----------------------
    scaler = StandardScaler()

    train_df[feature_cols] = scaler.fit_transform(
        train_df[feature_cols]
    )

    validation_df[feature_cols] = scaler.transform(
        validation_df[feature_cols]
    )

    test_df[feature_cols] = scaler.transform(
        test_df[feature_cols]
    )

    # -----------------------
    # Save scaler
    # -----------------------
    os.makedirs("DATA/processed", exist_ok=True)

    joblib.dump(
        scaler,
        "DATA/processed/scaler.pkl"
    )

    # -----------------------
    # Save scaled datasets
    # -----------------------
    train_df.to_csv(
        "DATA/processed/train_scaled.csv",
        index=False
    )

    validation_df.to_csv(
        "DATA/processed/validation_scaled.csv",
        index=False
    )

    test_df.to_csv(
        "DATA/processed/test_scaled.csv",
        index=False
    )

    print("\nScaling Complete.")

    print("\nTrain Shape:", train_df.shape)
    print("Validation Shape:", validation_df.shape)
    print("Test Shape:", test_df.shape)

    print("\nScaler saved to:")
    print("DATA/processed/scaler.pkl")


def main():
    """
    Run feature scaling.
    """
    scale_features()


if __name__ == "__main__":
    main()