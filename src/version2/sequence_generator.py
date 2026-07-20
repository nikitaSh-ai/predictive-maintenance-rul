"""
sequence_generator.py

Purpose:
Generate fixed length sequences for every
Version 2 dataset.
"""


import os

import numpy as np
import pandas as pd

SEQUENCE_LENGTH = 40

TARGET_COLUMN = "RUL_CLIPPED"
DATASETS = [
    "FD001",
    "FD002",
    "FD003",
    "FD004"
]
SPLITS = [
    "train",
    "validation",
    "test"
]

def create_output_directory():
    """
    Create the sequence output directory.
    """

    os.makedirs(
        "DATA/version2/sequences",
        exist_ok=True
    )



def load_scaled_dataset(dataset_name, split):
    """
    Load one scaled Version 2 dataset.
    """

    filename = (
        f"DATA/version2/scaled/"
        f"{dataset_name}_{split}.csv"
    )

    return pd.read_csv(filename)




def get_feature_columns(dataframe):
    """
    Return model feature columns.
    """

    excluded_columns = [
        "engine_id",
        "cycle",
        "max_cycle",
        "RUL",
        "RUL_CLIPPED"
    ]

    return [
        column
        for column in dataframe.columns
        if column not in excluded_columns
    ]




def create_engine_sequences(
    engine_dataframe,
    feature_columns
):
    """
    Generate sequences for one engine.
    """

    X = []
    y = []

    engine_dataframe = (
        engine_dataframe
        .sort_values("cycle")
    )

    features = engine_dataframe[
        feature_columns
    ].values

    targets = engine_dataframe[
        TARGET_COLUMN
    ].values

    for start in range(
        len(engine_dataframe)
        - SEQUENCE_LENGTH
        + 1
    ):

        end = start + SEQUENCE_LENGTH

        X.append(
            features[start:end]
        )

        y.append(
            targets[end - 1]
        )

    return X, y



def create_dataset_sequences(dataframe):
    """
    Generate sequences for one dataset.
    """

    feature_columns = get_feature_columns(
        dataframe
    )

    X_all = []
    y_all = []

    engine_ids = sorted(
        dataframe["engine_id"].unique()
    )

    for engine_id in engine_ids:

        engine_dataframe = dataframe[
            dataframe["engine_id"] == engine_id
        ]

        X_engine, y_engine = create_engine_sequences(
            engine_dataframe,
            feature_columns
        )

        X_all.extend(X_engine)
        y_all.extend(y_engine)

    X_all = np.array(
        X_all,
        dtype=np.float32
    )

    y_all = np.array(
        y_all,
        dtype=np.float32
    )

    return X_all, y_all




def save_sequences(
    dataset_name,
    split,
    X,
    y
):
    """
    Save sequence arrays.
    """

    np.save(
        f"DATA/version2/sequences/{dataset_name}_{split}_X.npy",
        X
    )

    np.save(
        f"DATA/version2/sequences/{dataset_name}_{split}_y.npy",
        y
    )




def load_sequences(
    dataset_name,
    split
):
    """
    Load saved sequence arrays.
    """

    X = np.load(
        f"DATA/version2/sequences/{dataset_name}_{split}_X.npy"
    )

    y = np.load(
        f"DATA/version2/sequences/{dataset_name}_{split}_y.npy"
    )

    return X, y


def main():

    X, y = load_sequences(
        "FD001",
        "train"
    )

    print("X Shape:", X.shape)
    print("y Shape:", y.shape)

    print()

    print("Sequence dtype:", X.dtype)
    print("Target dtype:", y.dtype)

    print()

    print("First target:", y[0])

    print("First sequence shape:", X[0].shape)


if __name__ == "__main__":
    main()