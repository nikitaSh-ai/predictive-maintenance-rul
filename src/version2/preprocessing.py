"""
preprocessing.py

Purpose:
Apply preprocessing to all Version 2 datasets.
"""
from sklearn.preprocessing import StandardScaler
import pandas as pd
import joblib
import os

def load_dataset(file_path):
    """
    Load a processed Version 2 dataset.
    """

    return pd.read_csv(file_path)


PROCESSED_DATA_PATH = "DATA/version2/processed"

DATASETS = [
    "FD001",
    "FD002",
    "FD003",
    "FD004"
]

SPLITS = [
    "train",
    "validation",
    "test"
]




def dataset_path(dataset, split):
    """
    Return processed dataset path.
    """

    return (
        f"{PROCESSED_DATA_PATH}/"
        f"{dataset}_{split}.csv"
    )



def get_feature_columns(dataframe):
    """
    Return feature columns used for model training.
    """

    exclude_columns = [
        "engine_id",
        "cycle",
        "max_cycle",
        "RUL",
        "RUL_CLIPPED"
    ]

    return [
        column
        for column in dataframe.columns
        if column not in exclude_columns
    ]





def load_training_dataset(dataset):
    """
    Load the training dataset for a NASA subset.
    """

    return load_dataset(
        dataset_path(dataset, "train")
    )


def load_all_training_datasets():
    """
    Load the training dataset of every NASA subset.

    Returns
    -------
    dict
        Dataset name -> DataFrame
    """

    datasets = {}

    for dataset in DATASETS:

        datasets[dataset] = load_training_dataset(
            dataset
        )

    return datasets





def combine_training_datasets(training_datasets):
    """
    Combine all training datasets into one dataframe.
    """

    combined = pd.concat(
        training_datasets.values(),
        ignore_index=True
    )

    return combined




def find_constant_features(dataframe):
    """
    Find features that have only one unique value.
    """

    feature_columns = get_feature_columns(dataframe)

    constant_features = []

    for feature in feature_columns:

        unique_values = dataframe[feature].nunique()

        if unique_values == 1:

            constant_features.append(feature)

    return constant_features




def print_constant_features(constant_features):
    """
    Display constant features.
    """

    print("\nConstant Features\n")

    for feature in constant_features:

        print(feature)

    print()

    print("Total:", len(constant_features))




def calculate_feature_variance(dataframe):
    """
    Calculate variance of all feature columns.
    """

    feature_columns = get_feature_columns(dataframe)

    variance = dataframe[feature_columns].var()

    return variance.sort_values()





def print_feature_variance(feature_variance):
    """
    Display feature variances.
    """

    print("\nFeature Variance\n")

    print(feature_variance)



def get_combined_training_dataset():
    """
    Load and combine all training datasets.
    """

    training_datasets = load_all_training_datasets()

    return combine_training_datasets(
        training_datasets
    )



def get_all_datasets():
    """
    Load every processed dataset.

    Returns
    -------
    dict
    """

    datasets = {}

    for dataset in DATASETS:

        datasets[dataset] = {}

        for split in SPLITS:

            datasets[dataset][split] = load_dataset(
                dataset_path(dataset, split)
            )

    return datasets







def get_model_features():
    """
    Return the features used by Version 2.
    """

    combined = get_combined_training_dataset()

    return get_feature_columns(combined)





def create_scaler():
    """
    Create a StandardScaler.
    """

    return StandardScaler()








def fit_global_scaler():
    """
    Fit a scaler using the combined
    Version 2 training data.
    """

    combined = get_combined_training_dataset()

    feature_columns = get_feature_columns(
        combined
    )

    scaler = create_scaler()

    scaler.fit(
        combined[feature_columns]
    )

    return scaler







def save_scaler(scaler):
    """
    Save the fitted scaler.
    """

    os.makedirs(
        "DATA/version2/models",
        exist_ok=True
    )

    joblib.dump(
        scaler,
        "DATA/version2/models/global_scaler.pkl"
    )

    print("Global scaler saved.")








def scale_dataset(dataframe, scaler):
    """
    Scale one dataset using the fitted scaler.
    """

    dataframe = dataframe.copy()

    feature_columns = get_feature_columns(
        dataframe
    )

    dataframe[feature_columns] = scaler.transform(
        dataframe[feature_columns]
    )

    return dataframe





def scale_all_datasets():
    """
    Scale every Version 2 dataset.
    """

    scaler = fit_global_scaler()

    datasets = get_all_datasets()

    scaled = {}

    for dataset in DATASETS:

        scaled[dataset] = {}

        for split in SPLITS:

            scaled[dataset][split] = scale_dataset(
                datasets[dataset][split],
                scaler
            )

    return scaled






def save_scaled_datasets(scaled_datasets):
    """
    Save all scaled datasets.
    """

    output_directory = (
        "DATA/version2/scaled"
    )

    os.makedirs(
        output_directory,
        exist_ok=True
    )

    for dataset in DATASETS:

        for split in SPLITS:

            scaled_datasets[dataset][split].to_csv(

                f"{output_directory}/"
                f"{dataset}_{split}.csv",

                index=False
            )

    print("\nScaled datasets saved.")





def verify_scaling():
    """
    Verify scaling using FD001 training data.
    """

    dataframe = pd.read_csv(
        "DATA/version2/scaled/FD001_train.csv"
    )

    feature_columns = get_feature_columns(
        dataframe
    )

    print("\nScaled Feature Means\n")

    print(
        dataframe[feature_columns]
        .mean()
        .head()
    )

    print("\nScaled Feature Standard Deviations\n")

    print(
        dataframe[feature_columns]
        .std()
        .head()
    )




def verify_global_scaling():
    """
    Verify scaling on the combined training dataset.
    """

    scaled = scale_all_datasets()

    combined = pd.concat(
        [
            scaled[dataset]["train"]
            for dataset in DATASETS
        ],
        ignore_index=True
    )

    feature_columns = get_feature_columns(
        combined
    )

    print("\nGlobal Means\n")
    print(
        combined[feature_columns]
        .mean()
        .head()
    )

    print("\nGlobal Std\n")
    print(
        combined[feature_columns]
        .std()
        .head()
    )



def main():

    scaled = scale_all_datasets()

    save_scaled_datasets(
        scaled
    )
    verify_global_scaling()
   
    
if __name__ == "__main__":
    main()