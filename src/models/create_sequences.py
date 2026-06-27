"""
create_sequences.py

Purpose:
Generate fixed-length sequences for model training.
"""

import numpy as np
import pandas as pd


SEQ_LENGTH = 30
TARGET_COLUMN = "RUL_CLIPPED"


def get_feature_columns(df):
    """
    Return feature columns used for sequence generation.
    """

    exclude_cols = [
        "engine_id",
        "cycle",
        "max_cycle",
        "RUL","RUL_CLIPPED"
    ]

    return [
        col
        for col in df.columns
        if col not in exclude_cols
    ]



def create_engine_sequences(engine_df, feature_cols):
    """
    Generate sequences for one engine.
    """

    X = []
    y = []

    engine_df = engine_df.sort_values("cycle")

    feature_array = engine_df[feature_cols].values
    target_array = engine_df[TARGET_COLUMN].values

    for i in range(len(engine_df) - SEQ_LENGTH + 1):

        sequence = feature_array[i:i + SEQ_LENGTH]

        target = target_array[i + SEQ_LENGTH - 1]

        X.append(sequence)
        y.append(target)

    return X, y






def create_dataset_sequences(df):
    """
    Generate sequences for an entire dataset
    (train, validation, or test).
    """

    feature_cols = get_feature_columns(df)

    X_all = []
    y_all = []

    engine_ids = sorted(df["engine_id"].unique())

    print(f"\nTotal Engines: {len(engine_ids)}")

    for engine_id in engine_ids:

        engine_df = df[df["engine_id"] == engine_id]

        X_engine, y_engine = create_engine_sequences(
            engine_df,
            feature_cols
        )

        X_all.extend(X_engine)
        y_all.extend(y_engine)

    X_all = np.array(X_all, dtype=np.float32)
    y_all = np.array(y_all, dtype=np.float32)

    return X_all, y_all




def main():
    """
    Generate sequences for train, validation,
    and test datasets.
    """

    # -----------------------
    # Load datasets
    # -----------------------
    train_df = pd.read_csv("DATA/processed/train_scaled.csv")

    validation_df = pd.read_csv(
        "DATA/processed/validation_scaled.csv"
    )

    test_df = pd.read_csv(
        "DATA/processed/test_scaled.csv"
    )

    # -----------------------
    # Generate sequences
    # -----------------------
    print("=" * 60)
    print("GENERATING TRAIN SEQUENCES")
    print("=" * 60)

    X_train, y_train = create_dataset_sequences(train_df)

    print("=" * 60)
    print("GENERATING VALIDATION SEQUENCES")
    print("=" * 60)

    X_validation, y_validation = create_dataset_sequences(
        validation_df
    )

    print("=" * 60)
    print("GENERATING TEST SEQUENCES")
    print("=" * 60)

    X_test, y_test = create_dataset_sequences(test_df)

    import os

    # -----------------------
    # Create output directory
    # -----------------------
    os.makedirs("DATA/sequences", exist_ok=True)

    # -----------------------
    # Save train sequences
    # -----------------------
    np.save("DATA/sequences/X_train.npy", X_train)
    np.save("DATA/sequences/y_train.npy", y_train)

    # -----------------------
    # Save validation sequences
    # -----------------------
    np.save("DATA/sequences/X_validation.npy", X_validation)
    np.save("DATA/sequences/y_validation.npy", y_validation)

    # -----------------------
    # Save test sequences
    # -----------------------
    np.save("DATA/sequences/X_test.npy", X_test)
    np.save("DATA/sequences/y_test.npy", y_test)

    print("\nSequences saved successfully.")

    # -----------------------
    # Verification only
    # -----------------------
    print("\nSequence Generation Complete.\n")

    print("Train X:", X_train.shape)
    print("Train y:", y_train.shape)

    print("\nValidation X:", X_validation.shape)
    print("Validation y:", y_validation.shape)

    print("\nTest X:", X_test.shape)
    print("Test y:", y_test.shape)




if __name__ == "__main__":
    main()