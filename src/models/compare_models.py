"""
compare_models.py

Purpose:
Compare Version 1 and Version 2 model performance.
"""

import os

import pandas as pd



def load_results():
    """
    Load evaluation results from both models.
    """

    version1 = pd.read_csv(
        "results/version1_results.csv"
    )

    version2 = pd.read_csv(
        "results/version2/generalized_results.csv"
    )

    return version1, version2






def merge_results(version1, version2):
    """
    Merge Version 1 and Version 2 results.
    """

    comparison = pd.concat(

        [version1, version2],

        ignore_index=True

    )

    return comparison






def save_comparison(comparison):
    """
    Save comparison results.
    """

    os.makedirs(
        "results/comparison",
        exist_ok=True
    )

    comparison.to_csv(

        "results/comparison/model_comparison.csv",

        index=False

    )

    print()

    print("Comparison report saved successfully.")

    print("results/comparison/model_comparison.csv")







def main():

    version1, version2 = load_results()

    comparison = merge_results(

        version1,
        version2

    )

    save_comparison(comparison)

    print()

    print(comparison)

    with open(
    "results/comparison/model_comparison.txt",
    "w"
) as file:

        file.write("MODEL COMPARISON REPORT\n")
        file.write("=" * 60 + "\n\n")

        file.write("Version 1 (FD001 Only)\n")
        file.write("-" * 40 + "\n")

        version1_row = comparison.iloc[0]

        file.write(f"Dataset : {version1_row['Dataset']}\n")
        file.write(f"MAE     : {version1_row['MAE']:.4f}\n")
        file.write(f"RMSE    : {version1_row['RMSE']:.4f}\n")
        file.write(f"R2      : {version1_row['R2']:.4f}\n\n")

        file.write("Version 2 (Generalized Model)\n")
        file.write("-" * 40 + "\n")

        version2_rows = comparison[
            comparison["Model"] == "Version 2"
        ]

        for _, row in version2_rows.iterrows():

            file.write(f"{row['Dataset']}\n")

            file.write(f"MAE  : {row['MAE']:.4f}\n")

            file.write(f"RMSE : {row['RMSE']:.4f}\n")

            file.write(f"R2   : {row['R2']:.4f}\n\n")




        file.write("\n")
        file.write("=" * 60 + "\n")
        file.write("Conclusion\n")
        file.write("=" * 60 + "\n\n")

        file.write(
    "Version 1 is specialized for the NASA FD001 operating condition and "
    "achieves the best performance on that dataset.\n\n"
)

        file.write(
    "Version 2 is designed for generalized Remaining Useful Life estimation "
    "across FD001, FD002, FD003, and FD004. Although its FD001 accuracy is "
    "slightly lower than the specialized model, it provides consistent "
    "performance across multiple operating conditions, making it suitable "
    "for real world predictive maintenance applications.\n"
)


if __name__ == "__main__":

    main()