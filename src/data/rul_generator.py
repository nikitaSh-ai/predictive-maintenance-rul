# This is where we create the target variable (RUL) for every engine.


"""
rul_generator.py

Purpose:
Generate Remaining Useful Life (RUL) for each engine
in the NASA CMAPSS dataset.
"""

import pandas as pd

from src.data.data_loader import load_data


def generate_rul(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate Remaining Useful Life (RUL) for each engine cycle.
    """

    max_cycles = (
        df.groupby("engine_id")["cycle"]
        .max()
        .reset_index()
        .rename(columns={"cycle": "max_cycle"})
    )

    df = df.merge(max_cycles, on="engine_id")

    df["RUL"] = df["max_cycle"] - df["cycle"]

    return df


def main():
    """
    Load the raw dataset, generate RUL,
    and display a sample.
    """

    df = load_data("DATA/raw/train_FD001.txt")

    df = generate_rul(df)

    print(df[["engine_id", "cycle", "max_cycle", "RUL"]].head(10))


if __name__ == "__main__":
    main()