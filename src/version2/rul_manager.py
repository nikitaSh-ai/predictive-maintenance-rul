"""
rul_manager.py

Purpose:
Generate RUL for all NASA datasets.
"""

from src.data.rul_generator import generate_rul
from src.version2.dataset_manager import load_all_datasets

RUL_MAX = 125

def generate_rul_for_all():
    """
    Generate RUL for every dataset.

    Returns
    -------
    dict
        Dataset name -> DataFrame
    """

    datasets = load_all_datasets()

    processed = {}

    for dataset_name, dataframe in datasets.items():

        dataframe = generate_rul(dataframe)

        dataframe["RUL_CLIPPED"] = dataframe["RUL"].clip(
        upper=RUL_MAX
        )

        processed[dataset_name] = dataframe

    return processed




def main():

    datasets = generate_rul_for_all()

    for name, df in datasets.items():

        print(name)

        print(df[[
            "engine_id",
            "cycle",
            "max_cycle",
            "RUL"
        ]].head())

        print("-" * 50)


if __name__ == "__main__":
    main()