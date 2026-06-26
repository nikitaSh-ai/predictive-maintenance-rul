#  only responsibility of this file: NASA text file -> Clean Pandas DataFrame
#   (No preprocessing. No feature engineering.No RUL.No scaling.)






import pandas as pd


COLUMN_NAMES = (
    ["engine_id", "cycle"]
    + [f"op_setting_{i}" for i in range(1, 4)]
    + [f"sensor_{i}" for i in range(1, 22)]
)


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load NASA CMAPSS dataset.

    Parameters:
        file_path (str): Path to dataset file.

    Returns:
        pd.DataFrame: Loaded dataframe.
    """

    df = pd.read_csv(
        file_path,
        sep=r"\s+",
        header=None
    )

    # Remove empty columns (NASA files contain two trailing blank columns)
    df = df.dropna(axis=1)

    df.columns = COLUMN_NAMES

    return df