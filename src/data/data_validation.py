# to verify the integrity of the raw dataset : 
from src.data.data_loader import load_data


def validate_data(df):
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


if __name__ == "__main__":
    df = load_data("DATA/raw/train_FD001.txt")
    validate_data(df)