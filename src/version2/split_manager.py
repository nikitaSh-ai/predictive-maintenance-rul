"""
split_manager.py

Purpose:
Create engine-level train, validation, and test splits
for all NASA datasets.
"""



import os
import json
import random
from src.version2.rul_manager import generate_rul_for_all

TRAIN_RATIO = 0.70
VALIDATION_RATIO = 0.15
TEST_RATIO = 0.15

RANDOM_SEED = 42


def create_output_directories():
    """
    Create Version 2 output directories.
    """

    os.makedirs(
        "DATA/version2/processed",
        exist_ok=True
    )

    os.makedirs(
        "DATA/version2/metadata",
        exist_ok=True
    )

def split_engine_ids(engine_ids):
    """
    Split engine IDs into train, validation and test sets.
    """

    random.seed(RANDOM_SEED)

    engine_ids = engine_ids.copy()

    random.shuffle(engine_ids)

    total = len(engine_ids)

    train_end = int(total * TRAIN_RATIO)

    validation_end = train_end + int(total * VALIDATION_RATIO)

    train_ids = engine_ids[:train_end]

    validation_ids = engine_ids[train_end:validation_end]

    test_ids = engine_ids[validation_end:]

    return train_ids, validation_ids, test_ids




def get_engine_ids(dataframe):
    """
    Return sorted engine IDs.
    """

    return sorted(
        dataframe["engine_id"].unique().tolist()
    )






def create_dataset(dataframe, engine_ids):
    """
    Create a dataset containing only the selected engines.
    """

    return dataframe[
        dataframe["engine_id"].isin(engine_ids)
    ].copy()




def create_all_splits():
    """
    Create train, validation and test datasets
    for all NASA datasets.

    Returns
    -------
    dict
        Dataset name -> split datasets and engine IDs.
    """

    datasets = generate_rul_for_all()

    split_results = {}

    for dataset_name, dataframe in datasets.items():

        engine_ids = get_engine_ids(dataframe)

        train_ids, validation_ids, test_ids = split_engine_ids(
            engine_ids
        )

        train_df = create_dataset(
            dataframe,
            train_ids
        )

        validation_df = create_dataset(
            dataframe,
            validation_ids
        )

        test_df = create_dataset(
            dataframe,
            test_ids
        )

        split_results[dataset_name] = {
            "train_ids": train_ids,
            "validation_ids": validation_ids,
            "test_ids": test_ids,
            "train_df": train_df,
            "validation_df": validation_df,
            "test_df": test_df
        }

    return split_results



def create_split_metadata(split_results):
    """
    Create metadata dictionary containing
    engine IDs for every dataset.
    """

    metadata = {}

    for dataset_name, result in split_results.items():

        metadata[dataset_name] = {

            "train": result["train_ids"],

            "validation": result["validation_ids"],

            "test": result["test_ids"]
        }

    return metadata





def save_split_metadata(metadata):
    """
    Save engine split metadata.
    """

    with open(
        "DATA/version2/metadata/engine_split.json",
        "w"
    ) as file:

        json.dump(
            metadata,
            file,
            indent=4
        )

    print("\nEngine split metadata saved.")






def save_processed_datasets(split_results):
    """
    Save train, validation and test datasets
    for every NASA dataset.
    """

    output_directory = "DATA/version2/processed"

    for dataset_name, result in split_results.items():

        result["train_df"].to_csv(
            f"{output_directory}/{dataset_name}_train.csv",
            index=False
        )

        result["validation_df"].to_csv(
            f"{output_directory}/{dataset_name}_validation.csv",
            index=False
        )

        result["test_df"].to_csv(
            f"{output_directory}/{dataset_name}_test.csv",
            index=False
        )

    print("\nProcessed datasets saved.")




def verify_saved_datasets():
    """
    Verify that all saved datasets can be loaded.
    """

    import pandas as pd

    print("\nVerifying saved datasets...\n")

    datasets = [
        "FD001",
        "FD002",
        "FD003",
        "FD004"
    ]

    splits = [
        "train",
        "validation",
        "test"
    ]

    for dataset in datasets:

        for split in splits:

            file_path = (
                f"DATA/version2/processed/"
                f"{dataset}_{split}.csv"
            )

            df = pd.read_csv(file_path)

            print(
                f"{dataset}_{split}: {df.shape}"
            )






def main():

    create_output_directories()

    split_results = create_all_splits()

    metadata = create_split_metadata(split_results)

    save_split_metadata(metadata)

    save_processed_datasets(split_results)

    for dataset_name, result in split_results.items():

      train_ids = result["train_ids"]
      validation_ids = result["validation_ids"]
      test_ids = result["test_ids"]

      train_df = result["train_df"]
      validation_df = result["validation_df"]
      test_df = result["test_df"]

      print("\n" + "=" * 50)
      print(dataset_name)
      print("=" * 50)

      print("Train:", len(train_ids))
      print("Validation:", len(validation_ids))
      print("Test:", len(test_ids))

      print()

      print("Train Shape:", train_df.shape)
      print("Validation Shape:", validation_df.shape)
      print("Test Shape:", test_df.shape)

      verify_saved_datasets()

    

       




if __name__ == "__main__":
    main()