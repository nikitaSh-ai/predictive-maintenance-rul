"""
model_comparison.py

Purpose:
Compare all prediction models
used in the project.
"""


import os
import pandas as pd
import matplotlib.pyplot as plt



def load_metrics(file_path):
    """
    Load MAE, RMSE and R²
    from a metrics file.
    """

    metrics = {}

    with open(file_path, "r") as file:

        for line in file:

            if "MAE" in line:
                metrics["MAE"] = float(line.split(":")[1])

            elif "RMSE" in line:
                metrics["RMSE"] = float(line.split(":")[1])

            elif "R2" in line:
                metrics["R2"] = float(line.split(":")[1])

    return metrics

def main():

    print("=" * 60)
    print("MODEL COMPARISON")
    print("=" * 60)


    # ---------------------------------
    # Metrics File Paths
    # ---------------------------------

    rf_metrics_path = "results/random_forest_metrics.txt"
    xgb_metrics_path = "results/Xgboost/xgboost_metrics.txt"
    gru_metrics_path = "results/gru_metrics.txt"


    # ---------------------------------
    # Verify Files
    # ---------------------------------

    print("\nChecking Metrics Files...")

    print(
    "Random Forest :",
    os.path.exists(rf_metrics_path)
    )

    print(
    "XGBoost       :",
    os.path.exists(xgb_metrics_path)
    )

    print(
    "GRU           :",
    os.path.exists(gru_metrics_path)
    )





    # ---------------------------------
    # Load Metrics
    # ---------------------------------

    rf_metrics = load_metrics(
    rf_metrics_path
    )

    xgb_metrics = load_metrics(
    xgb_metrics_path
    )

    gru_metrics = load_metrics(
    gru_metrics_path
    )

    print("\nRandom Forest Metrics")
    print(rf_metrics)

    print("\nXGBoost Metrics")
    print(xgb_metrics)

    print("\nGRU Metrics")
    print(gru_metrics)




    # ---------------------------------
    # Build Comparison Table
    # ---------------------------------

    comparison_df = pd.DataFrame({

        "Model": [
        "Random Forest",
        "XGBoost",
        "GRU"
        ],

       "MAE": [
        rf_metrics["MAE"],
        xgb_metrics["MAE"],
        gru_metrics["MAE"]
        ],

        "RMSE": [
        rf_metrics["RMSE"],
        xgb_metrics["RMSE"],
        gru_metrics["RMSE"]
        ],

        "R2": [
        rf_metrics["R2"],
        xgb_metrics["R2"],
        gru_metrics["R2"]
       ]  

    })

    print("\nComparison Table")

    print(comparison_df)



    # ---------------------------------
    # Save Comparison Table
    # ---------------------------------

    comparison_df.to_csv(
    "results/model_comparison.csv",
    index=False
    )

    print(
    "\nComparison table saved successfully."
    )



    # ---------------------------------
    # Best Model
    # ---------------------------------

    best_model = comparison_df.loc[
    comparison_df["R2"].idxmax()
    ]

    print("\nBest Model")

    print(best_model)



    # ---------------------------------
    # Final Summary
    # ---------------------------------

    print("\n" + "=" * 60)
    print("FINAL MODEL SELECTION")
    print("=" * 60)

    print(
    f"Best Model : {best_model['Model']}"
    )

    print(
    f"MAE        : {best_model['MAE']:.4f}"
    )

    print(
    f"RMSE       : {best_model['RMSE']:.4f}"
    )

    print(
    f"R²         : {best_model['R2']:.4f}"
    )




    # ---------------------------------
    # Create Plot Folder
    # ---------------------------------

    os.makedirs(
    "results/plots",
    exist_ok=True
    )

    # ---------------------------------
    # MAE Comparison
    # ---------------------------------

    plt.figure(figsize=(8, 5))

    bars=plt.bar(
    comparison_df["Model"],
    comparison_df["MAE"]
    )

    for bar in bars:

     height = bar.get_height()

     plt.text(
        bar.get_x() + bar.get_width()/2,
        height,
        f"{height:.2f}",
        ha="center",
        va="bottom"
     )

    plt.title("Model Comparison (MAE)")
    plt.ylabel("MAE")

    plt.tight_layout()

    plt.savefig(
    "results/plots/model_comparison_mae.png",
    dpi=300
    )

    plt.close()

    print("\nMAE comparison plot saved.")




    # ---------------------------------
    # RMSE Comparison
    # ---------------------------------

    plt.figure(figsize=(8, 5))

    bars=plt.bar(
    comparison_df["Model"],
    comparison_df["RMSE"]
    )
    for bar in bars:

     height = bar.get_height()

     plt.text(
        bar.get_x() + bar.get_width()/2,
        height,
        f"{height:.2f}",
        ha="center",
        va="bottom"
      )

    plt.title("Model Comparison (RMSE)")
    plt.ylabel("RMSE")

    plt.tight_layout()

    plt.savefig(
    "results/plots/model_comparison_rmse.png",
    dpi=300
    )

    plt.close()

    print("\nRMSE comparison plot saved.")




    # ---------------------------------
    # R² Comparison
    # ---------------------------------

    plt.figure(figsize=(8, 5))

    bars = plt.bar(
    comparison_df["Model"],
    comparison_df["R2"]
    )

    for bar in bars:

     height = bar.get_height()

     plt.text(
        bar.get_x() + bar.get_width()/2,
        height,
        f"{height:.4f}",
        ha="center",
        va="bottom"
     )

    plt.title("Model Comparison (R²)")
    plt.ylabel("R²")

    plt.tight_layout()

    plt.savefig(
    "results/plots/model_comparison_r2.png",
    dpi=300
    )

    plt.close()

    print("\nR² comparison plot saved.")




if __name__ == "__main__":
    main()