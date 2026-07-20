"""
dataset_manager.py

Purpose:
Load all NASA C-MAPSS datasets for Version 2.
"""

import pandas as pd

from src.data.data_loader import load_data

FD001_PATH = "DATA/raw/train_FD001.txt"
FD002_PATH = "DATA/raw/train_FD002.txt"
FD003_PATH = "DATA/raw/train_FD003.txt"
FD004_PATH = "DATA/raw/train_FD004.txt"


def load_all_datasets():
    """
    Load all four NASA C-MAPSS datasets.

    Returns:
        dict: Dataset name -> DataFrame
    """

    datasets = {
        "FD001": load_data(FD001_PATH),
        "FD002": load_data(FD002_PATH),
        "FD003": load_data(FD003_PATH),
        "FD004": load_data(FD004_PATH),
    }

    return datasets



def main():
    """
    Verify all datasets load successfully.
    """

    datasets = load_all_datasets()

    for name, df in datasets.items():
        print(f"{name}: {df.shape}")



if __name__ == "__main__":
    main()