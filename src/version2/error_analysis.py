"""
error_analysis.py

Purpose:
Analyze prediction errors of the
generalized GRU model.
"""

import os
import torch
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


RESULTS_PATH = (
    "results/version2/"
    "generalized_results.csv"
)


def load_results():
    """
    Load evaluation results.
    """

    return pd.read_csv(
        RESULTS_PATH
    )





def print_summary(results):
    """
    Print summary statistics.
    """

    print("\nSummary Statistics\n")

    print(
        results[
            ["MAE", "RMSE", "R2"]
        ].describe()
    )









def plot_metric(
    results,
    metric,
    ylabel,
    filename
):
    """
    Plot one evaluation metric.
    """

    plt.figure(figsize=(7, 5))

    plt.bar(
        results["Dataset"],
        results[metric]
    )

    plt.title(
        f"{metric} Across NASA Datasets"
    )

    plt.xlabel("Dataset")

    plt.ylabel(ylabel)

    plt.grid(axis="y")

    plt.tight_layout()

    plt.savefig(
        f"results/version2/{filename}",
        dpi=300
    )

    plt.show()








def main():

    results = load_results()
    print(results)

    print_summary(results)
    plot_metric(
    results,
    metric="MAE",
    ylabel="MAE",
    filename="mae_comparison.png"
)
    
    plot_metric(
    results,
    metric="RMSE",
    ylabel="RMSE",
    filename="rmse_comparison.png"
)

    plot_metric(
    results,
    metric="R2",
    ylabel="R²",
    filename="r2_comparison.png"
)
    
   

if __name__ == "__main__":
    main()