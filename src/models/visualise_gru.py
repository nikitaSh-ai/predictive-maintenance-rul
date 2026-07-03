"""
visualize_gru.py

Purpose:
Generate visualization plots
for the trained GRU model.
"""

import numpy as np
import matplotlib.pyplot as plt
import torch
import os
import joblib
from torch.utils.data import (
    TensorDataset,
    DataLoader
)

import pandas as pd

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from src.models.gru_model import GRUModel


def main():

    print("=" * 60)
    print("GRU VISUALIZATION")
    print("=" * 60)

    # ---------------------------------
    # Load Test Sequences
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
    # Convert to Tensors
    # ---------------------------------

    X_test = torch.tensor(
        X_test,
        dtype=torch.float32
    )

    y_test = torch.tensor(
        y_test,
        dtype=torch.float32
    )

    print("\nTensor Information")
    print("X_test :", X_test.shape)
    print("y_test :", y_test.shape)

    # ---------------------------------
    # Create Dataset
    # ---------------------------------

    test_dataset = TensorDataset(
        X_test,
        y_test
    )

    print("\nTest Dataset Size")
    print(len(test_dataset))

    # ---------------------------------
    # DataLoader
    # ---------------------------------

    test_loader = DataLoader(
        test_dataset,
        batch_size=64,
        shuffle=False
    )

    print("\nNumber of Test Batches")
    print(len(test_loader))

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

    print("\nBest GRU model loaded successfully.")

    # ---------------------------------
    # Prediction
    # ---------------------------------

    all_predictions = []
    all_actuals = []

    with torch.no_grad():

        for X_batch, y_batch in test_loader:

            X_batch = X_batch.to(device)

            predictions = model(X_batch)

            all_predictions.extend(
                predictions.squeeze().cpu().numpy()
            )

            all_actuals.extend(
                y_batch.numpy()
            )

    all_predictions = np.array(
        all_predictions
    )

    all_actuals = np.array(
        all_actuals
    )



    # ---------------------------------
    # Create Output Folder
    # ---------------------------------
    os.makedirs(
    "results/gru",
    exist_ok=True
    )


    # ---------------------------------
    # Prediction Summary
    # ---------------------------------

    print("\nPrediction Summary")
    print("Number of Predictions :", len(all_predictions))
    print("Number of Actuals     :", len(all_actuals))

    print("\nPrediction Range")
    print(
        np.min(all_predictions),
        np.max(all_predictions)
    )

    print("\nActual Range")
    print(
        np.min(all_actuals),
        np.max(all_actuals)
    )


    # ---------------------------------
    # Prediction vs Actual Plot
    # ---------------------------------

    plt.figure(figsize=(8, 6))

    plt.scatter(
    all_actuals,
    all_predictions,
    alpha=0.5
    )

    plt.plot(
    [all_actuals.min(), all_actuals.max()],
    [all_actuals.min(), all_actuals.max()],
    "r--",
    linewidth=2
    )

    plt.xlabel("Actual RUL")
    plt.ylabel("Predicted RUL")
    plt.title("GRU Prediction vs Actual")

    plt.tight_layout()

    plt.savefig(
    "results/gru/prediction_vs_actual.png",
    dpi=300
    )

    plt.close()

    print("Prediction vs Actual plot saved.")



    # ---------------------------------
    # Residual Plot
    # ---------------------------------

    residuals = all_actuals - all_predictions

    plt.figure(figsize=(8, 6))

    plt.scatter(
    all_predictions,
    residuals,
    alpha=0.5
)

    plt.axhline(
    y=0,
    linestyle="--",
    linewidth=2,
    color="red"
    )

    plt.xlabel("Predicted RUL")
    plt.ylabel("Residual")
    plt.title("GRU: Residual Plot")

    plt.tight_layout()

    plt.savefig(
    "results/gru/residual_plot_gru.png",
    dpi=300
    )

    plt.close()

    print("Residual plot saved.")





    # ---------------------------------
   # Save Prediction CSV
    # ---------------------------------

    prediction_df = pd.DataFrame({
    "Actual_RUL": all_actuals,
    "Predicted_RUL": all_predictions
    })

    prediction_df.to_csv(
    "results/gru/gru_predictions.csv",
    index=False
    )

    print("Prediction CSV saved.")



    # ---------------------------------
    # Evaluation Metrics
    # ---------------------------------

    mae = mean_absolute_error(
    all_actuals,
    all_predictions
    )

    rmse = np.sqrt(
    mean_squared_error(
        all_actuals,
        all_predictions
    )
    )

    r2 = r2_score(
    all_actuals,
    all_predictions
    )

    print("\nEvaluation Metrics")
    print(f"MAE  : {mae:.4f}")
    print(f"RMSE : {rmse:.4f}")
    print(f"R²   : {r2:.4f}")


    # ---------------------------------
    # Save Metrics
    # ---------------------------------

    with open(
    "results/gru/gru_metrics.txt",
    "w"
    ) as file:

      file.write(
        f"MAE  : {mae:.4f}\n"
      )

      file.write(
        f"RMSE : {rmse:.4f}\n"
      )

      file.write(
        f"R2   : {r2:.4f}\n"
       )

    print("Metrics saved.")


    # ---------------------------------
   # Load Training History
   # ---------------------------------

    history = joblib.load(
    "results/gru/training_history.pkl"
     )

    train_loss = history["train_loss"]
    validation_loss = history["validation_loss"]



  
    # ---------------------------------
    # Training Curve
    # ---------------------------------

    plt.figure(figsize=(8,6))

    epochs = range(
    1,
    len(train_loss)+1
    )

    plt.plot(
    epochs,
    train_loss,
    label="Training Loss"
    )

    plt.plot(
    epochs,
    validation_loss,
    label="Validation Loss"
    )

    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.title("GRU Training History")

    plt.legend()

    plt.tight_layout()

    plt.savefig(
    "results/gru/training_curve.png",
    dpi=300
    )

    plt.close()

    print("Training curve saved.")

if __name__ == "__main__":
    main()