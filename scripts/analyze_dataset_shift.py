"""
analyze_dataset_shift.py

Purpose:
Analyze distribution differences between the NASA C-MAPSS datasets
(FD001, FD002, FD003, and FD004).

This script is read-only.
It does not modify any data or models.
"""

import pandas as pd

COLUMN_NAMES = [
    "engine_id",
    "cycle",
    "op_setting_1",
    "op_setting_2",
    "op_setting_3",
]

COLUMN_NAMES.extend([f"sensor_{i}" for i in range(1, 22)])

FD001_PATH = "DATA/raw/train_FD001.txt"
FD002_PATH = "DATA/raw/train_FD002.txt"
FD003_PATH = "DATA/raw/train_FD003.txt"
FD004_PATH = "DATA/raw/train_FD004.txt"

fd001 = pd.read_csv(
    FD001_PATH,
    sep=r"\s+",
    header=None,
    names=COLUMN_NAMES
)
# print(fd001.head())

fd002 = pd.read_csv(
    FD002_PATH,
    sep=r"\s+",
    header=None,
    names=COLUMN_NAMES
)
# print(fd002.head())


fd003 = pd.read_csv(
    FD003_PATH,
    sep=r"\s+",
    header=None,
    names=COLUMN_NAMES
)

fd004 = pd.read_csv(
    FD004_PATH,
    sep=r"\s+",
    header=None,
    names=COLUMN_NAMES
)


def print_dataset_summary(dataset_name, dataframe):
    """
    Print basic information about a dataset.
    """

    print("\n" + "=" * 50)
    print(dataset_name)
    print("=" * 50)

    print(f"Rows    : {dataframe.shape[0]}")
    print(f"Columns : {dataframe.shape[1]}")
    print(f"Engines : {dataframe['engine_id'].nunique()}")
    print(f"Missing : {dataframe.isnull().sum().sum()}")



print_dataset_summary("FD001", fd001)
print_dataset_summary("FD002", fd002)
print_dataset_summary("FD003", fd003)
print_dataset_summary("FD004", fd004)