# Now we'll combine the first three stages: Engine Split + RUL Generation + Dataset Saving
# This will create the three datasets that every later stage (feature engineering, scaling, RF, XGBoost, GRU) will use.





"""
build_datasets.py

Purpose:
Build Train, Validation, and Test datasets
using the engine-level split.
"""

import os
import json

from src.data.data_loader import load_data
from src.data.rul_generator import generate_rul


def build_datasets():
    """
    Build train, validation, and test datasets.
    """

    # -----------------------
    # Load raw dataset
    # -----------------------
    df = load_data("DATA/raw/train_FD001.txt")

    # -----------------------
    # Generate RUL
    # -----------------------
    df = generate_rul(df)

    # -----------------------
    # Load engine split
    # -----------------------
    with open("DATA/processed/engine_split.json", "r") as f:
        split = json.load(f)

    train_engines = set(split["train"])
    validation_engines = set(split["validation"])
    test_engines = set(split["test"])

    # -----------------------
    # Create datasets
    # -----------------------
    train_df = df[df["engine_id"].isin(train_engines)].copy()

    validation_df = df[df["engine_id"].isin(validation_engines)].copy()

    test_df = df[df["engine_id"].isin(test_engines)].copy()

    # -----------------------
    # Save datasets
    # -----------------------
    os.makedirs("DATA/processed", exist_ok=True)

    train_df.to_csv("DATA/processed/train.csv", index=False)
    validation_df.to_csv("DATA/processed/validation.csv", index=False)
    test_df.to_csv("DATA/processed/test.csv", index=False)

    # -----------------------
    # Verification
    # -----------------------
    print("Train shape:", train_df.shape)
    print("Validation shape:", validation_df.shape)
    print("Test shape:", test_df.shape)


def main():
    """
    Run dataset creation pipeline.
    """
    build_datasets()


if __name__ == "__main__":
    main()