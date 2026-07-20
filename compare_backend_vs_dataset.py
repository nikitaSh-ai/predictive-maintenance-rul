import numpy as np
import pandas as pd
import joblib

SEQUENCE_LENGTH = 40

df = pd.read_csv(
    "DATA/version2/scaled/FD004_train.csv"
)

engine = df[df["engine_id"] == 1]

sequence = engine.tail(SEQUENCE_LENGTH)

feature_columns = [
    c for c in df.columns
    if c not in [
        "engine_id",
        "cycle",
        "max_cycle",
        "RUL",
        "RUL_CLIPPED",
    ]
]

dataset_tensor = sequence[feature_columns].values

saved_sequences = np.load(
    "DATA/version2/sequences/FD004_train_X.npy"
)

differences = np.abs(
    saved_sequences - dataset_tensor
).max(axis=(1, 2))

closest_index = differences.argmin()

saved_tensor = saved_sequences[closest_index]

print("Closest saved sequence index:", closest_index)

print(
    "Maximum difference:",
    differences[closest_index],
)
