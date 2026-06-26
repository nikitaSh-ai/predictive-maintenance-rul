# This script will compute the number of unique values of every feature , identify constant features automatically ,save the list

"""
check_constant_features.py

Purpose:
Automatically identify constant features in the NASA CMAPSS FD001 dataset.
These features carry no information and will be removed before model training.
"""

import pandas as pd

# -----------------------
# Load training dataset
# -----------------------
train_df = pd.read_csv("DATA/processed/train.csv")

print("=" * 60)
print("CONSTANT FEATURE ANALYSIS")
print("=" * 60)

# Columns that are NOT sensor/features
exclude_cols = [
    "engine_id",
    "cycle",
    "RUL",
    "max_cycle"
]

feature_cols = [
    col for col in train_df.columns
    if col not in exclude_cols
]

constant_features = []

print("\nChecking feature variability...\n")

for feature in feature_cols:

    unique_values = train_df[feature].nunique()

    print(f"{feature:<15} Unique Values: {unique_values}")

    if unique_values == 1:
        constant_features.append(feature)

print("\n" + "=" * 60)

print("Constant Features Found:")

for feature in constant_features:
    print(feature)

print("\nTotal Constant Features:", len(constant_features))

# -----------------------
# Save list for later use
# -----------------------
with open("DATA/processed/constant_features.txt", "w") as f:
    for feature in constant_features:
        f.write(feature + "\n")

print("\nSaved to:")
print("DATA/processed/constant_features.txt")