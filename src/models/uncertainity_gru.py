"""
uncertainty_gru.py

Purpose:
Estimate prediction uncertainty
using Monte Carlo Dropout.
"""

import os
import pandas as pd
import torch
import numpy as np
import matplotlib.pyplot as plt

from src.models.gru_model import GRUModel

def enable_dropout(model):
    """
    Enable dropout layers during inference.
    """

    for module in model.modules():

        if isinstance(module, torch.nn.Dropout):

            module.train()



def main():

    print("=" * 60)
    print("GRU UNCERTAINTY ESTIMATION")
    print("=" * 60)

    # ---------------------------------
    # Device
    # ---------------------------------

    device = torch.device(
        "cuda"
        if torch.cuda.is_available()
        else "cpu"
    )

    print(f"\nDevice: {device}")




    # ---------------------------------
    # Load Model
    # ---------------------------------

    model = GRUModel(
        input_size=17,
        hidden_size=128,
        num_layers=1
    )

    model.load_state_dict(
        torch.load(
            "models/best_gru.pth",
            map_location=device
        )
    )

    model.to(device)
    model.eval()

    enable_dropout(model)

    print("\nBest GRU model loaded successfully.")



    # ---------------------------------
    # Enable Dropout During Inference
    # ---------------------------------

    #model.train()


    # ---------------------------------
    # Load Test Data
    # ---------------------------------

    X_test = np.load(
        "DATA/sequences/X_test.npy"
    )

    y_test = np.load(
        "DATA/sequences/y_test.npy"
    )

    print("\nLoaded Test Data")
    print("X_test :", X_test.shape)
    print("y_test :", y_test.shape)



    # ---------------------------------
    # Monte Carlo Settings
    # ---------------------------------

    num_samples = 50

    print(f"\nMonte Carlo Samples : {num_samples}")



    # ---------------------------------
    # Convert to Tensor
    # ---------------------------------

    X_test = torch.tensor(
        X_test,
        dtype=torch.float32
    )

    y_test = torch.tensor(
        y_test,
        dtype=torch.float32
    )



    # ---------------------------------
    # Store Results
    # ---------------------------------

    mean_predictions = []

    uncertainty_scores = []

    actual_values = []


   # ---------------------------------
   # Monte Carlo Prediction
   # ---------------------------------

    with torch.no_grad():

     for sample, actual in zip(X_test, y_test):

        sample = sample.unsqueeze(0).to(device)
        predictions = []

        for _ in range(num_samples):

            prediction = model(sample)

            predictions.append(
                prediction.item()
            )
       
    


        predictions = np.array(predictions)    
        prediction_mean = predictions.mean()

        prediction_std = predictions.std()

        mean_predictions.append(prediction_mean)

        uncertainty_scores.append(prediction_std)
        actual_values.append(actual.item())


    # ---------------------------------
    # Prediction Summary
    # ---------------------------------

    print("\nPrediction Summary")
    print("Mean Predictions :", len(mean_predictions))
    print("Uncertainty Scores :", len(uncertainty_scores))
    print("Actual Values :", len(actual_values))


    # ---------------------------------
    # Convert to NumPy Arrays
    # ---------------------------------

    mean_predictions = np.array(mean_predictions)

    uncertainty_scores = np.array(uncertainty_scores)

    actual_values = np.array(actual_values)



    # ---------------------------------
    # Uncertainty Summary
    # ---------------------------------

    print("\nUncertainty Summary")
    print(
    f"Average Uncertainty : {uncertainty_scores.mean():.4f}"
)
    print(
    f"Minimum Uncertainty : {uncertainty_scores.min():.4f}"
    )
    print(
    f"Maximum Uncertainty : {uncertainty_scores.max():.4f}"
    )


    # ---------------------------------
    # Save Results
    # ---------------------------------

    results = pd.DataFrame(
    {
        "Actual_RUL": actual_values,
        "Predicted_RUL": mean_predictions,
        "Uncertainty": uncertainty_scores
    }
    )

    # ---------------------------------
    # Confidence Interval
    # ---------------------------------

    results["Lower_Bound"] = (
    results["Predicted_RUL"]
    - 1.96 * results["Uncertainty"]
    )

    results["Upper_Bound"] = (
    results["Predicted_RUL"]
    + 1.96 * results["Uncertainty"]
    )



    results.to_csv(
    "results/gru_uncertainty_results.csv",
    index=False
    )

    print("\nUncertainty results saved successfully.")

    # ---------------------------------
    # Preview Results
    # ---------------------------------

    print("\nFirst Five Predictions")

    print(
    results.head()
    )

    print("\nConfidence Interval Preview")

    print(
    results[
        [
            "Predicted_RUL",
            "Lower_Bound",
            "Upper_Bound"
        ]
    ].head()
    )




    # ---------------------------------
    # Confidence Category
    # ---------------------------------

    conditions = [
    results["Uncertainty"] < 3,
    results["Uncertainty"] < 5
    ]

    categories = [
    "High",
    "Medium"
    ]

    results["Confidence"] = np.select(
    conditions,
    categories,
    default="Low"
    )



    # ---------------------------------
    # Confidence Distribution
    # ---------------------------------

    print("\nConfidence Distribution")

    print(results["Confidence"].value_counts())



    # ---------------------------------
    # Uncertainty Histogram
    # ---------------------------------

    plt.figure(figsize=(8,5))

    plt.hist(
    results["Uncertainty"],
    bins=20,
    edgecolor="black"
    )

    plt.title(
    "Distribution of Prediction Uncertainty"
    )

    plt.xlabel(
    "Uncertainty (Standard Deviation)"
     )

    plt.ylabel(
    "Number of Samples"
    )

    plt.tight_layout()

    os.makedirs(
    "results/plots",
    exist_ok=True
    )   

    plt.savefig(
    "results/plots/gru_uncertainty_histogram.png",
    dpi=300
    )

    plt.close()

    print(
    "\nUncertainty histogram saved successfully."
    )




    # ---------------------------------
    # Prediction vs Uncertainty
    # ---------------------------------

    plt.figure(figsize=(8,5))

    plt.scatter(
    results["Predicted_RUL"],
    results["Uncertainty"],
    alpha=0.35,
    s=25
    )

    plt.title(
    "Predicted RUL vs Prediction Uncertainty"
    )

    plt.xlabel(
    "Predicted RUL"
    )

    plt.ylabel(
    "Uncertainty (Standard Deviation)"
    )

    plt.tight_layout()

    plt.savefig(
    "results/plots/gru_prediction_uncertainty_scatter.png",
    dpi=300
    )

    plt.close()

    print(
    "Prediction vs Uncertainty plot saved successfully."
    )


if __name__ == "__main__":
    main()