import pandas as pd

# Load training dataset only
train_df = pd.read_csv("DATA/processed/train.csv")

print("=" * 60)
print("TRAIN DATASET OVERVIEW")
print("=" * 60)

print("\nShape:")
print(train_df.shape)

print("\nColumns:")
print(train_df.columns.tolist())

print("\nMissing Values:")
print(train_df.isnull().sum().sum())

print("\nFeature Summary:")
print(train_df.describe().T)