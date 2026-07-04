"""
explain_gru.py

Purpose:
Explain GRU predictions
using SHAP.
"""

import torch
import shap
import numpy as np

from src.models.gru_model import GRUModel


def predict_fn(data, model, device):
    """
    Prediction function for SHAP.
    """
    data = torch.tensor(
    data,
    dtype=torch.float32
    ).to(device)

    model.eval()

    with torch.no_grad():

        predictions = model(data)
    return predictions.cpu().numpy()

def main():

    # ---------------------------------
    # Device
    # ---------------------------------

    device = torch.device(
        "cuda"
        if torch.cuda.is_available()
        else "cpu"
    )

   

    print("=" * 60)
    print("GRU SHAP EXPLAINABILITY")
    print("=" * 60)

    print(f"\nDevice: {device}")


    # ---------------------------------
    # Load Trained GRU Model
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
    # Load Data
    # ---------------------------------

    X_train = np.load(
    "DATA/sequences/X_train.npy"
    )

    X_test = np.load(
    "DATA/sequences/X_test.npy"
    )

    y_test = np.load(
    "DATA/sequences/y_test.npy"
    )

    print("\nLoaded Data")
    print("X_train :", X_train.shape)
    print("X_test  :", X_test.shape)
    print("y_test  :", y_test.shape)
   


    # ---------------------------------
    # Select Background Samples
    # ---------------------------------

    np.random.seed(42)

    indices = np.random.choice(
        len(X_train),
        size=100,
        replace=False
    )

    background_data = X_train[indices]

    print("\nBackground Dataset")
    print("Background Shape :", background_data.shape)




    # ---------------------------------
    # Convert Background Data to Tensor
    # ---------------------------------

    background_data = torch.tensor(
        background_data,
        dtype=torch.float32
    ).to(device)

    print("\nBackground Tensor")
    print(background_data.shape)
    print(background_data.dtype)
    

    # ---------------------------------
    # Select Samples to Explain
    # ---------------------------------

    explain_data = X_test[:100]

    print("\nExplain Dataset")
    print("Explain Shape :", explain_data.shape)


    # ---------------------------------
    # Convert Explain Data to Tensor
    # ---------------------------------

    explain_data = torch.tensor(
        explain_data,
        dtype=torch.float32
    ).to(device)

    print("\nExplain Tensor")
    print(explain_data.shape)
    print(explain_data.dtype)
   


   
if __name__ == "__main__":
    main()