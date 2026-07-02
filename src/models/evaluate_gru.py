"""
evaluate_gru.py

Purpose:
Evaluate the trained GRU model
on the test dataset.
"""

import torch
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from torch.utils.data import (
    TensorDataset,
    DataLoader
)

from src.models.gru_model import GRUModel






def load_test_data():
    """
    Load the test sequences.
    """

    X_test = np.load("DATA/sequences/X_test.npy")
    y_test = np.load("DATA/sequences/y_test.npy")

    return X_test, y_test
    

def main():

    print("=" * 60)
    print("GRU EVALUATION")
    print("=" * 60)

    X_test, y_test = load_test_data()
    X_test = torch.FloatTensor(X_test)
    y_test = torch.FloatTensor(y_test)

    test_dataset = TensorDataset(
    X_test,
    y_test
    )
    
    test_loader = DataLoader(
    test_dataset,
    batch_size=64,
    shuffle=False
    )

    # -----------------------
    # Initialize GRU Model
    # -----------------------

    model = GRUModel(
    input_size=17,
    hidden_size=64,
    num_layers=1
    )

    device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
    )
    model = model.to(device)

   



    # -----------------------
    # Load Best Model
    # -----------------------

    model.load_state_dict(
    torch.load(
        "models/best_gru.pth",
        map_location=device
    )
    )
    model.eval()




    # -----------------------
    # Prediction Containers
    # -----------------------

    all_preds = []
    all_actuals = []

    # -----------------------
    # Predict on Test Set
    # -----------------------

    with torch.no_grad():

      for X_batch, y_batch in test_loader:

        X_batch = X_batch.to(device)
        y_batch = y_batch.to(device)

        predictions = model(X_batch)

        all_preds.append(
            predictions.cpu().numpy()
        )

        all_actuals.append(
            y_batch.cpu().numpy()
        )

      all_preds = np.concatenate( all_preds).flatten()
      all_actuals = np.concatenate(all_actuals).flatten()


    # -----------------------
    # Evaluation Metrics
    # -----------------------

    mae = mean_absolute_error(
    all_actuals,
    all_preds
    )

    rmse = np.sqrt(
    mean_squared_error(
        all_actuals,
        all_preds
    )
    )

    r2 = r2_score(
    all_actuals,
    all_preds
    )



    with open(
    "results/gru_metrics.txt",
    "w"
    ) as file:

      file.write("GRU Evaluation Metrics\n")
      file.write("======================\n\n")

      file.write(f"MAE  : {mae:.4f}\n")
      file.write(f"RMSE : {rmse:.4f}\n")
      file.write(f"R2   : {r2:.4f}\n")


    prediction_df = pd.DataFrame({

    "Actual_RUL": all_actuals,
    "Predicted_RUL": all_preds
    })
    prediction_df.to_csv(

    "results/gru_predictions.csv",

    index=False
    )


    # -----------------------
    # Prediction vs Actual Plot
    # -----------------------

    plt.figure(figsize=(10, 6))

    plt.scatter(
    all_actuals,
    all_preds,
    alpha=0.6
    )

    plt.plot(
    [all_actuals.min(), all_actuals.max()],
    [all_actuals.min(), all_actuals.max()],
    linestyle="--",
    color="red",
    label="Perfect Prediction"
    )

    plt.xlabel("Actual RUL")

    plt.ylabel("Predicted RUL")

    plt.title("GRU Prediction vs Actual")

    plt.legend()

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
    "results/gru_prediction_vs_actual.png"
    )

    plt.close()




    # -----------------------
   # Residual Plot
   # -----------------------

    residuals = all_actuals - all_preds

    plt.figure(figsize=(10, 6))

    plt.scatter(
    all_preds,
    residuals,
    alpha=0.6
    )

    plt.axhline(
    y=0,
    color="red",
    linestyle="--"
    )

    plt.xlabel("Predicted RUL")

    plt.ylabel("Residual")

    plt.title("GRU Residual Plot")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
    "results/gru_residual_plot.png"
    )

    plt.close()


    

   
    print("\nLoaded Test Data")

    print("X_test :", X_test.shape)
    print("y_test :", y_test.shape)

    print("\nTensor Information")

    print("X_test :", X_test.shape)
    print("y_test :", y_test.shape)

    print("\nTest Dataset Size")
    print(len(test_dataset))

    print("\nNumber of Test Batches")
    print(len(test_loader))



    print("\nDevice:", device)
    print("\nBest GRU model loaded successfully.")




    print("\nPrediction Summary")

    print("Number of Predictions :", len(all_preds))
    print("Number of Actuals     :", len(all_actuals))

    print("\nPrediction Range")
    print(all_preds.min(), all_preds.max())

    print("\nActual Range")
    print(all_actuals.min(), all_actuals.max())




    print("\n=========================")
    print("TEST EVALUATION RESULTS")
    print("=========================")

    print(f"MAE  : {mae:.4f}")
    print(f"RMSE : {rmse:.4f}")
    print(f"R2   : {r2:.4f}")


if __name__ == "__main__":
    main()





 