"""
feature_analysis.py

Purpose:
Perform basic exploratory analysis of the
training dataset.
"""

import pandas as pd


def analyze_features():
    """
    Display basic information about the training dataset.
    """

    # Load training dataset
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


def main():
    """
    Run feature analysis.
    """
    analyze_features()


if __name__ == "__main__":
    main()