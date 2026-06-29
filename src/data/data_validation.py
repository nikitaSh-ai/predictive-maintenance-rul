"""
data_validation.py

Purpose:
Validate the raw NASA CMAPSS FD001 dataset before preprocessing.
"""

from src.data.data_loader import load_data


def validate_data(df):
    """
    Perform basic validation checks on the dataset.
    """

    print("=" * 50)
    print("DATA VALIDATION REPORT")
    print("=" * 50)

    print("\nDataset Shape:")
    print(df.shape)

    print("\nMissing Values:")
    print(df.isnull().sum().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nNumber of Engines:")
    print(df["engine_id"].nunique())

    print("\nCycle Range:")
    print("Min:", df["cycle"].min())
    print("Max:", df["cycle"].max())


def main():
    """
    Load the raw dataset and perform validation.
    """

    df = load_data("DATA/raw/train_FD001.txt")
    validate_data(df)


if __name__ == "__main__":
    main()