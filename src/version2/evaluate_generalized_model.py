"""
evaluate_generalized_model.py

Purpose:
Evaluate the Version 2 generalized GRU model.
"""
import os
import pandas as pd
import numpy as np
import torch
import matplotlib.pyplot as plt
from torch.utils.data import TensorDataset, DataLoader
from src.version2.generalized_gru import GeneralizedGRU
from src.version2.utils import load_model

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

TEST_DATASETS = [
    "FD001",
    "FD002",
    "FD003",
    "FD004"
]


def load_test_sequences(dataset_name):
    """
    Load one test dataset.
    """

    X = np.load(
        f"DATA/version2/sequences/{dataset_name}_test_X.npy"
    )

    y = np.load(
        f"DATA/version2/sequences/{dataset_name}_test_y.npy"
    )

    return X, y










def predict(model, X, device):
    """
    Generate predictions for one dataset.
    """

    X = torch.FloatTensor(X)

    dataset = TensorDataset(X)

    loader = DataLoader(
        dataset,
        batch_size=64,
        shuffle=False
    )

    predictions = []

    with torch.no_grad():

        for (X_batch,) in loader:

            X_batch = X_batch.to(device)

            output = model(X_batch)

            predictions.extend(
                output.squeeze(1).cpu().numpy()
            )

    return np.array(predictions)





def evaluate_predictions(
    y_true,
    predictions
):
    """
    Compute regression metrics.
    """

    mae = mean_absolute_error(
        y_true,
        predictions
    )

    rmse = np.sqrt(
        mean_squared_error(
            y_true,
            predictions
        )
    )

    r2 = r2_score(
        y_true,
        predictions
    )

    return mae, rmse, r2





def predict_dataset(
    model,
    X,
    device
):
    """
    Predict one dataset.
    """

    model.eval()

    with torch.no_grad():

        X = torch.FloatTensor(X).to(device)

        predictions = model(X)

        predictions = (
        predictions
        .cpu()
        .numpy()
        .flatten()
    )

    return predictions


def plot_actual_vs_predicted(
    prediction_results
):
    """
    Plot Actual vs Predicted RUL.
    """
    plt.figure(
    figsize=(7,7)
)
    
    for dataset in prediction_results:

        actual = prediction_results[dataset]["actual"]

        predicted = prediction_results[dataset]["predicted"]

        plt.scatter(actual,predicted,s=10,alpha=0.4,label=dataset)




    plt.plot(
    [0,125],
    [0,125],
    color="red",
    linestyle="--",
    linewidth=2,
    label="Perfect Prediction")


    plt.xlabel("Actual RUL")

    plt.ylabel("Predicted RUL")

    plt.title(
    "Actual vs Predicted RUL")

    plt.legend()

    plt.grid(True)

    plt.tight_layout()

    os.makedirs(
    "results/version2",
    exist_ok=True)

    plt.savefig(
    "results/version2/actual_vs_predicted.png",
    dpi=300,
    bbox_inches="tight")

    plt.show()
    





def plot_residual_histogram(
    prediction_results
):
    """
    Plot residual distribution.
    """

    plt.figure(
    figsize=(8,5))


    for dataset in prediction_results:

        actual = prediction_results[dataset]["actual"]

        predicted = prediction_results[dataset]["predicted"]

        residuals = predicted - actual

        plt.hist(
          residuals,
          bins=40,
          alpha=0.4,
          label=dataset
        )

    plt.axvline(
    0,
    color="red",
    linestyle="--",
    linewidth=2
    )



    plt.ylabel("Frequency")

    plt.title(
        "Residual Distribution Across NASA Datasets"
    )

    plt.legend()

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        "results/version2/residual_histogram.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()





def plot_residuals_vs_actual(
    prediction_results
):
    """
    Plot residuals against actual RUL.
    """

    plt.figure(
        figsize=(8,6)
    )

    for dataset in prediction_results:

      actual = prediction_results[dataset]["actual"]

      predicted = prediction_results[dataset]["predicted"]

      residuals = predicted - actual

      plt.scatter(
          actual,
          residuals,
          s=10,
          alpha=0.4,
          label=dataset
      )



    plt.axhline(
    0,
    color="red",
    linestyle="--",
    linewidth=2
)
    
    plt.xlabel("Actual RUL")
    plt.ylabel("Residual Error")
    plt.title(
    "Residual Error vs Actual RUL"
)
    
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(
    "results/version2/residual_vs_actual.png",
    dpi=300,
    bbox_inches="tight"
)
    plt.show()





def plot_dataset_comparison(results):
    """
    Compare MAE across datasets.
    """

    datasets = list(results.keys())

    maes = [
        results[d][0]
        for d in datasets
    ]

    plt.figure(figsize=(7,5))
    plt.bar(
    datasets,
    maes
)
    plt.ylabel("MAE")
    plt.title(
    "Generalized Model Performance"
)
    plt.grid(
    axis="y"
)
    plt.tight_layout()
    plt.savefig(
    "results/version2/dataset_comparison.png",
    dpi=300,
    bbox_inches="tight"
)
    plt.show()








def main():

    print("=" * 60)
    print("GENERALIZED MODEL EVALUATION")
    print("=" * 60)

    device = torch.device(
        "cuda" if torch.cuda.is_available() else "cpu"
    )

    model = load_model(device)

    print()

    print("Device:", device)

    print()

    print("Model Loaded Successfully")

    print(model)

    print()
    print()

    results = {}
    prediction_results = {}

    for dataset in TEST_DATASETS:

      X, y = load_test_sequences(dataset)

      predictions = predict(
        model,
        X,
        device)

      mae, rmse, r2 = evaluate_predictions(
        y,
        predictions)
      

      prediction_results[dataset] = {
    "actual": y,
    "predicted": predictions
}

      results[dataset] = (
        mae,
        rmse,
        r2)
      
    print()

    print("=" * 60)
    print("GENERALIZED MODEL RESULTS")
    print("=" * 60)

    for dataset, metrics in results.items():

      mae, rmse, r2 = metrics

      print()

      print(dataset)

      print(f"MAE  : {mae:.4f}")

      print(f"RMSE : {rmse:.4f}")

      print(f"R²   : {r2:.4f}")
    


    results_df = pd.DataFrame(
    {
        "Dataset": list(results.keys()),
        "MAE": [m[0] for m in results.values()],
        "RMSE": [m[1] for m in results.values()],
        "R2": [m[2] for m in results.values()]
    })


    os.makedirs(
    "results/version2",
    exist_ok=True
)
    
    results_df.to_csv(
    "results/version2/generalized_results.csv",
    index=False
)
    
    print()

    print(
    "Results saved to:"
)

    print(
    "results/version2/generalized_results.csv"
)
    
    plot_actual_vs_predicted(
    prediction_results
)
    

    plot_residual_histogram(
    prediction_results
)
    plot_residuals_vs_actual(
    prediction_results
)
    plot_dataset_comparison(
    results
)

if __name__ == "__main__":
    main()