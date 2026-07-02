"""
train_gru.py

Purpose:
Train the GRU model for
Remaining Useful Life prediction.
"""

import torch
import numpy as np
import pandas as pd
import torch.nn as nn
import matplotlib.pyplot as plt

from src.models.gru_model import GRUModel
from torch.utils.data import(
     TensorDataset,DataLoader
      )
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def load_sequences():
    """
    Load train, validation and test sequences.
    """

    X_train = np.load("DATA/sequences/X_train.npy")
    y_train = np.load("DATA/sequences/y_train.npy")

    X_validation = np.load("DATA/sequences/X_validation.npy")
    y_validation = np.load("DATA/sequences/y_validation.npy")

    X_test = np.load("DATA/sequences/X_test.npy")
    y_test = np.load("DATA/sequences/y_test.npy")

    return (
        X_train,
        y_train,
        X_validation,
        y_validation,
        X_test,
        y_test
    )

def train_one_epoch(
    model,
    train_loader,
    criterion,
    optimizer,
    device
):
    """
    Train the model for one epoch.
    """

    model.train()

    running_loss = 0.0

    for X_batch, y_batch in train_loader:

        X_batch = X_batch.to(device)
        y_batch = y_batch.to(device)

        predictions = model(X_batch)

        loss = criterion(
            predictions,
            y_batch.unsqueeze(1)
        )

        optimizer.zero_grad()

        loss.backward()

        torch.nn.utils.clip_grad_norm_(
            model.parameters(),
            max_norm=1.0
        )

        optimizer.step()

        running_loss += loss.item()

    average_loss = (
        running_loss /
        len(train_loader)
    )

    return average_loss

    



def validate_one_epoch(
    model,
    validation_loader,
    criterion,
    device
):
    """
    Evaluate the model for one epoch.
    """

    model.eval()
    running_loss = 0.0

    with torch.no_grad():

        for X_batch, y_batch in validation_loader:

            X_batch = X_batch.to(device)
            y_batch = y_batch.to(device)

            predictions = model(X_batch)

            loss = criterion(
                predictions,
                y_batch.unsqueeze(1)
            )

            running_loss += loss.item()

    average_loss = (
        running_loss /
        len(validation_loader)
    )

    return average_loss




def main():

    (
    X_train,
    y_train,
    X_validation,
    y_validation,
    X_test,
    y_test
     ) = load_sequences()
    
    print("=" * 60)
    print("GRU TRAINING")
    print("=" * 60)

    # -----------------------
    # Convert to Torch Tensors
    # -----------------------

    X_train = torch.FloatTensor(X_train)
    y_train = torch.FloatTensor(y_train)

    X_validation = torch.FloatTensor(X_validation)
    y_validation = torch.FloatTensor(y_validation)

    X_test = torch.FloatTensor(X_test)
    y_test = torch.FloatTensor(y_test)


    # -----------------------
# Create TensorDatasets
# -----------------------

    train_dataset = TensorDataset(
    X_train,
    y_train
     )

    validation_dataset = TensorDataset(
    X_validation,
    y_validation
     )

    test_dataset = TensorDataset(
    X_test,
    y_test
     )
    
# -----------------------
# Create DataLoaders
# -----------------------

    batch_size = 64
    train_loader = DataLoader(
    train_dataset,
    batch_size=batch_size,
    shuffle=True
     )

    validation_loader = DataLoader(
    validation_dataset,
    batch_size=batch_size,
    shuffle=False
      )

    test_loader = DataLoader(
    test_dataset,
    batch_size=batch_size,
    shuffle=False
     )
    


    print("\nSequence Shapes")

    print("X_train      :", X_train.shape)
    print("y_train      :", y_train.shape)

    print("X_validation :", X_validation.shape)
    print("y_validation :", y_validation.shape)

    print("X_test       :", X_test.shape)
    print("y_test       :", y_test.shape)


    print("\nTensor Types")

    print("X_train      :", X_train.dtype)
    print("y_train      :", y_train.dtype)

    print("X_validation :", X_validation.dtype)
    print("y_validation :", y_validation.dtype)

    print("X_test       :", X_test.dtype)
    print("y_test       :", y_test.dtype)

    print("\nDataset Sizes")

    print("Train      :", len(train_dataset))
    print("Validation :", len(validation_dataset))
    print("Test       :", len(test_dataset))

    print("\nNumber of Batches")

    print("Train      :", len(train_loader))
    print("Validation :", len(validation_loader))
    print("Test       :", len(test_loader))

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

    print("Device:", device)



    print("\nModel Initialized Successfully.")
    print(model)


# -----------------------
# Define Loss Function
# -----------------------

    criterion = nn.MSELoss()

    print("\nLoss Function:")
    print(criterion)

# -----------------------
# Define Optimizer
# -----------------------

    optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
      )

    print("\nOptimizer:")
    print(optimizer)


    train_loss_history = []
    validation_loss_history = []
    best_val_loss = float("inf")
    patience = 3
    early_stop_counter = 0

    num_epochs = 20
    for epoch in range(num_epochs):

        # -----------------------
        # Train One Epoch
        # -----------------------

        train_loss = train_one_epoch(
            model=model,
            train_loader=train_loader,
            criterion=criterion,
            optimizer=optimizer,
            device=device
        )


        validation_loss = validate_one_epoch(
            model=model,
            validation_loader=validation_loader,
            criterion=criterion,
            device=device
             )
        


        train_loss_history.append(train_loss)
        validation_loss_history.append(validation_loss)

        print(f"\nEpoch {epoch + 1}/{num_epochs}")

        print(f"Training Loss : {train_loss:.6f}")

        print(f"Validation Loss : {validation_loss:.6f}")

        
        if validation_loss < best_val_loss:
            best_val_loss = validation_loss
            torch.save(model.state_dict(), "models/best_gru.pth")
            print("Best model saved!")
            early_stop_counter = 0
        else:
            early_stop_counter += 1

        if early_stop_counter >= patience:
             print("Early stopping triggered!")
             break
        
    
    model.load_state_dict(torch.load("models/best_gru.pth"))
    model.eval()
    print("\nTraining completed successfully.")

    print("\nTraining History")

    print("Training Losses")
    print(train_loss_history)

    print("\nValidation Losses")
    print(validation_loss_history)



    plt.figure(figsize=(8, 5))

    plt.plot(
    train_loss_history,
    label="Training Loss"
    )

    plt.plot(
    validation_loss_history,
    label="Validation Loss"
    )

    plt.xlabel("Epoch")

    plt.ylabel("Loss")

    plt.title("GRU Training History")

    plt.legend()

    plt.grid(True)

    plt.savefig("results/training_loss.png")

    plt.show()




if __name__ == "__main__":
     main()
