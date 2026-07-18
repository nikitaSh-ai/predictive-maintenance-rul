"""
analyze_dataset_shift.py

Purpose:
Analyze distribution differences between the NASA C-MAPSS datasets
(FD001, FD002, FD003, and FD004).

This script is read-only.
It does not modify any data or models.
"""

import pandas as pd
import numpy as np

import os

COLUMN_NAMES = [
    "engine_id",
    "cycle",
    "op_setting_1",
    "op_setting_2",
    "op_setting_3",
]

COLUMN_NAMES.extend([f"sensor_{i}" for i in range(1, 22)])
FEATURE_COLUMNS = COLUMN_NAMES[2:]
ACTIVE_FEATURES = [
    "op_setting_1",
    "op_setting_2",
    "sensor_2",
    "sensor_3",
    "sensor_4",
    "sensor_6",
    "sensor_7",
    "sensor_8",
    "sensor_9",
    "sensor_11",
    "sensor_12",
    "sensor_13",
    "sensor_14",
    "sensor_15",
    "sensor_17",
    "sensor_20",
    "sensor_21"
]
print("\nActive Features:", len(ACTIVE_FEATURES))



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



DATASETS = {
    "FD001": fd001,
    "FD002": fd002,
    "FD003": fd003,
    "FD004": fd004
}



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





def calculate_feature_statistics(dataframe, feature_name):
    """
    Calculate basic statistics for a single feature.
    """

    return {
    "Feature": feature_name,
    "Mean": dataframe[feature_name].mean(),
    "Standard Deviation": dataframe[feature_name].std(),
    "Minimum": dataframe[feature_name].min(),
    "Maximum": dataframe[feature_name].max()
    }





def compare_feature_across_datasets(feature_name, datasets):
    """
    Compare one feature across all four datasets.
    """

    comparison = []

    for dataset_name, dataframe in datasets.items():

        statistics = calculate_feature_statistics(
        dataframe,
        feature_name
        )

        statistics["Dataset"] = dataset_name

        comparison.append(statistics)

    comparison = pd.DataFrame(comparison)

    return comparison




def generate_statistics_report(feature_list):
    """
    Generate statistics for all features across all datasets.
    """

    all_statistics = pd.DataFrame()

    for feature in feature_list:

        comparison = compare_feature_across_datasets(feature,DATASETS)

        all_statistics = pd.concat(
            [all_statistics, comparison],
            ignore_index=True
        )

    return all_statistics





def calculate_mean_drift(statistics_report, feature_list):
    """
    Calculate mean drift between FD001 and other datasets.
    """

    drift_scores = []

    for feature in feature_list:

        feature_statistics = statistics_report[
            statistics_report["Feature"] == feature
        ]

        fd001_mean = feature_statistics[
            feature_statistics["Dataset"] == "FD001"
        ]["Mean"].values[0]

        drift = 0

        for dataset in ["FD002", "FD003", "FD004"]:

            dataset_mean = feature_statistics[
                feature_statistics["Dataset"] == dataset
            ]["Mean"].values[0]

            drift += abs(dataset_mean - fd001_mean)

        drift_scores.append({
            "Feature": feature,
            "Mean Drift": drift
        })

    return pd.DataFrame(drift_scores)







def analyze_operating_conditions():
    """
    Analyze the operating settings for all datasets.
    """

    operating_columns = [
        "op_setting_1",
        "op_setting_2",
        "op_setting_3"
    ]

    for dataset_name, dataframe in [
        ("FD001", fd001),
        ("FD002", fd002),
        ("FD003", fd003),
        ("FD004", fd004)
    ]:

        print(f"\n{'='*50}")
        print(dataset_name)
        print("="*50)

        print(
            dataframe[operating_columns].describe()
        )





def analyze_sensor_summary():
    """
    Analyze sensor statistics across datasets.
    """

    sensor_columns = COLUMN_NAMES[5:]

    for dataset_name, dataframe in [
        ("FD001", fd001),
        ("FD002", fd002),
        ("FD003", fd003),
        ("FD004", fd004)
    ]:

        print(f"\n{'=' * 60}")
        print(f"{dataset_name} Sensor Summary")
        print("=" * 60)

        print(
            dataframe[sensor_columns].describe().T.head()
        )





def generate_correlation_matrix(dataframe, feature_list):
    """
    Generate the correlation matrix for the selected features.
    """

    correlation_matrix = dataframe[feature_list].corr()

    return correlation_matrix



def save_correlation_matrix(
    correlation_matrix,
    filename
):
    """
    Save a correlation matrix as a CSV file.
    """

    correlation_matrix.to_csv(
        filename
    )






# fd001_statistics = calculate_feature_statistics(fd001, "op_setting_1")

raw_statistics_report = generate_statistics_report(
    FEATURE_COLUMNS
)

active_statistics_report = generate_statistics_report(
    ACTIVE_FEATURES
)

print(raw_statistics_report.head())

raw_drift_report = calculate_mean_drift(
    raw_statistics_report,
    FEATURE_COLUMNS
)

active_drift_report = calculate_mean_drift(
    active_statistics_report,
    ACTIVE_FEATURES
)

print("\nFeature Drift Report")


drift_report = raw_drift_report.sort_values(
    by="Mean Drift",
    ascending=False
)

print("\nTop Drift Features")

print("\nTop Raw Feature Drift")

print(raw_drift_report.head(10))

print("\nTop Active Feature Drift")

print(active_drift_report.head(10))


raw_statistics_report.to_csv(
    "reports/version2/raw_statistics_report.csv",
    index=False
)

active_statistics_report.to_csv(
    "reports/version2/active_statistics_report.csv",
    index=False
)





raw_drift_report.to_csv(
    "reports/version2/raw_mean_drift_report.csv",
    index=False
)

active_drift_report.to_csv(
    "reports/version2/active_mean_drift_report.csv",
    index=False
)



print("\nRaw statistics report saved successfully.")
print("Active statistics report saved successfully.")

print("\nRaw mean drift report saved successfully.")
print("Active mean drift report saved successfully.")



#analyze_operating_conditions()
analyze_sensor_summary()

os.makedirs(
    "reports/version2/correlations",
    exist_ok=True
)

correlation_matrices = {}

for dataset_name, dataframe in DATASETS.items():

    correlation_matrix = generate_correlation_matrix(
        dataframe,
        ACTIVE_FEATURES
    )

    correlation_matrices[
        dataset_name
    ] = correlation_matrix

    save_correlation_matrix(
        correlation_matrix,
        f"reports/version2/correlations/{dataset_name}_correlation.csv"
    )


print("\nStored Correlation Matrices:")

print(correlation_matrices.keys())   

def calculate_correlation_difference(
    reference_matrix,
    comparison_matrix
    ):
         """
         Calculate the absolute difference between
         two correlation matrices.
         """

         difference_matrix = abs(
             reference_matrix - comparison_matrix
         )
         return difference_matrix


     
    
def save_difference_matrix(
       difference_matrix,
       filename
    ):
      """
      Save a correlation difference matrix.
      """

      difference_matrix.to_csv(
          filename
       )
    



print("\nCorrelation matrices generated successfully.")

os.makedirs(
    "reports/version2/correlation_differences",
    exist_ok=True
)

reference_matrix = correlation_matrices["FD001"]



for dataset_name in ["FD002", "FD003", "FD004"]:

    difference_matrix = calculate_correlation_difference(
        reference_matrix,
        correlation_matrices[dataset_name]
    )

    save_difference_matrix(
        difference_matrix,
        f"reports/version2/correlation_differences/FD001_vs_{dataset_name}.csv"
    )

def extract_top_correlation_changes(
    difference_matrix,
    top_n=20
):
    """
    Extract the feature pairs with the
    largest correlation differences.
    """

    rows = []

    columns = difference_matrix.columns

    for i in range(len(columns)):

        for j in range(i + 1, len(columns)):

            rows.append({
                "Feature 1": columns[i],
                "Feature 2": columns[j],
                "Difference": difference_matrix.iloc[i, j]
            })

    rows = pd.DataFrame(rows)

    rows = rows.sort_values(
       by="Difference",
       ascending=False
)

    return rows.head(top_n)

print("\nCorrelation difference matrices generated successfully.")


def classify_feature_stability(
    drift_report
):
    """
    Classify active features based on
    their mean drift.
    """

    stability = drift_report.copy()

    
    high_threshold = stability["Mean Drift"].quantile(0.66)

    low_threshold = stability["Mean Drift"].quantile(0.33)

    for index in stability.index:

      drift = stability.loc[index, "Mean Drift"]
 
      if drift <= low_threshold:

        stability.loc[index, "Stability"] = "High"

      elif drift <= high_threshold:

        stability.loc[index, "Stability"] = "Medium"

      else:

        stability.loc[index, "Stability"] = "Low"

    stability = stability.sort_values(
    by="Mean Drift"
    )

    return stability






def print_phase_a_summary():

    print("\n" + "=" * 60)
    print("PHASE A OBSERVATIONS")
    print("=" * 60)

    print("1. FD001 and FD003 have very similar operating conditions.")

    print("2. FD002 and FD004 have significantly different operating conditions.")

    print("3. Several active features exhibit substantial distribution drift.")

    print("4. Some active features remain stable across all datasets.")

    print("5. Version 1 preprocessing is dataset specific.")

    print("6. Generalized preprocessing is justified for Version 2.")



for dataset_name in ["FD002", "FD003", "FD004"]:

    difference_matrix = calculate_correlation_difference(
        reference_matrix,
        correlation_matrices[dataset_name]
    )

    top_changes = extract_top_correlation_changes(
        difference_matrix
    )

    top_changes.to_csv(
        f"reports/version2/top_correlation_changes/FD001_vs_{dataset_name}_Top20.csv",
        index=False
    )

print("\nTop correlation change reports generated successfully.")

feature_stability = classify_feature_stability(
    active_drift_report
)

print("\nFeature Stability")

print(feature_stability.head())

feature_stability.to_csv(
    "reports/version2/feature_stability/feature_stability_report.csv",
    index=False
)

print("\nFeature stability report saved successfully.")

print("\nFeature Stability Summary")

print(
    feature_stability["Stability"].value_counts()
)


print_phase_a_summary()