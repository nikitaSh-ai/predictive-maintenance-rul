"""
feature_selection.py

Purpose:
Remove constant features automatically from the train,
validation and test datasets.
"""

import os
import pandas as pd

# -----------------------
# Load datasets
# -----------------------
train_df = pd.read_csv("DATA/processed/train.csv")
validation_df = pd.read_csv("DATA/processed/validation.csv")
test_df = pd.read_csv("DATA/processed/test.csv")

# -----------------------
# Load constant features
# -----------------------
with open("DATA/processed/constant_features.txt", "r") as f:
    constant_features = [
        line.strip()
        for line in f
        if line.strip()
    ]

print("=" * 60)
print("FEATURE SELECTION")
print("=" * 60)

print("\nRemoving constant features:")
for feature in constant_features:
    print(feature)

# -----------------------
# Drop features
# -----------------------
train_selected = train_df.drop(columns=constant_features)
validation_selected = validation_df.drop(columns=constant_features)
test_selected = test_df.drop(columns=constant_features)

# -----------------------
# Save datasets
# -----------------------
os.makedirs("DATA/processed", exist_ok=True)

train_selected.to_csv(
    "DATA/processed/train_selected.csv",
    index=False
)

validation_selected.to_csv(
    "DATA/processed/validation_selected.csv",
    index=False
)

test_selected.to_csv(
    "DATA/processed/test_selected.csv",
    index=False
)

print("\nSaved selected datasets.")

print("\nShapes:")
print("Train:", train_selected.shape)
print("Validation:", validation_selected.shape)
print("Test:", test_selected.shape)