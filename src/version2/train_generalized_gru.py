"""
train_generalized_gru.py

Purpose:
Train a generalized GRU model using
all NASA datasets.
"""

import os

import torch.nn as nn

from torch.optim.lr_scheduler import ReduceLROnPlateau 
import joblib
import numpy as np
import torch
import matplotlib.pyplot as plt

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
from torch.utils.data import DataLoader
from src.version2.generalized_gru import GeneralizedGRU

from torch.utils.data import TensorDataset

DATASETS = [
    "FD001",
    "FD002",
    "FD003",
    "FD004"
]

TRAIN_SPLIT = "train"
VALIDATION_SPLIT = "validation"

SEQUENCE_DIRECTORY = "DATA/version2/sequences"

def load_sequences(dataset_name, split):
    """
    Load one sequence dataset.
    """

    X = np.load(
        f"{SEQUENCE_DIRECTORY}/{dataset_name}_{split}_X.npy"
    )

    y = np.load(
        f"{SEQUENCE_DIRECTORY}/{dataset_name}_{split}_y.npy"
    )

    return X, y


def load_all_training_sequences():
    """
    Load training sequences from all datasets.
    """

    X_list = []
    y_list = []

    for dataset_name in DATASETS:

        X, y = load_sequences(
            dataset_name,
            TRAIN_SPLIT
        )

        X_list.append(X)
        y_list.append(y)

    return X_list, y_list




def load_all_validation_sequences():
    """
    Load validation sequences from all datasets.
    """

    X_list = []
    y_list = []

    for dataset_name in DATASETS:

        X, y = load_sequences(
            dataset_name,
            VALIDATION_SPLIT
        )

        X_list.append(X)
        y_list.append(y)

    return X_list, y_list


def combine_training_sequences(
    X_list,
    y_list
):
    """
    Combine all training datasets into
    one generalized training dataset.
    """

    X = np.concatenate(
        X_list,
        axis=0
    )

    y = np.concatenate(
        y_list,
        axis=0
    )

    return X, y


def combine_validation_sequences(
    X_list,
    y_list
):
    """
    Combine all validation datasets into
    one generalized validation dataset.
    """

    X = np.concatenate(
        X_list,
        axis=0
    )

    y = np.concatenate(
        y_list,
        axis=0
    )

    return X, y




def convert_to_tensors(
    X,
    y
):
    """
    Convert NumPy arrays to PyTorch tensors.
    """

    X = torch.FloatTensor(X)

    y = torch.FloatTensor(y)

    return X, y




def create_tensor_datasets(
    X_train,
    y_train,
    X_validation,
    y_validation
):
    """
    Create PyTorch TensorDatasets.
    """

    train_dataset = TensorDataset(
        X_train,
        y_train
    )

    validation_dataset = TensorDataset(
        X_validation,
        y_validation
    )

    return train_dataset, validation_dataset





def create_dataloaders(
    train_dataset,
    validation_dataset,
    batch_size=64
):
    """
    Create DataLoaders for training and validation.
    """

    generator = torch.Generator()

    generator.manual_seed(42)

    train_loader = DataLoader(
        train_dataset,
        batch_size=batch_size,
        shuffle=True,
        generator=generator
    )

    validation_loader = DataLoader(
        validation_dataset,
        batch_size=batch_size,
        shuffle=False
    )

    return train_loader, validation_loader





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



def load_best_model(
    model,
    model_path,
    device
):
    """
    Load the best saved generalized model.
    """

    model.load_state_dict(
        torch.load(
            model_path,
            map_location=device
        )
    )

    model.eval()

    return model

def main():

    # -----------------------
    # Load Training Data
    # -----------------------
    X_train_list, y_train_list = load_all_training_sequences()

    X_train, y_train = combine_training_sequences(
        X_train_list,
        y_train_list
    )

    # -----------------------
    # Load Validation Data
    # -----------------------
    X_validation_list, y_validation_list = (
        load_all_validation_sequences()
    )

    X_validation, y_validation = (
        combine_validation_sequences(
            X_validation_list,
            y_validation_list
        )
    )

    # -----------------------
    # Convert to Tensors
    # -----------------------
    X_train, y_train = convert_to_tensors(
        X_train,
        y_train
    )

    X_validation, y_validation = convert_to_tensors(
        X_validation,
        y_validation
    )

    # -----------------------
    # TensorDatasets
    # -----------------------
    train_dataset, validation_dataset = (
        create_tensor_datasets(
            X_train,
            y_train,
            X_validation,
            y_validation
        )
    )

    # -----------------------
    # DataLoaders
    # -----------------------
    train_loader, validation_loader = (
        create_dataloaders(
            train_dataset,
            validation_dataset
        )
    )

    print("Train Batches:", len(train_loader))
    print("Validation Batches:", len(validation_loader))

    print()

    X_batch, y_batch = next(iter(train_loader))

    print("Batch X Shape:", X_batch.shape)
    print("Batch y Shape:", y_batch.shape)

    print()

    print("Batch Data Type:", X_batch.dtype)
    print("Target Data Type:", y_batch.dtype)


    device = torch.device(
        "cuda" if torch.cuda.is_available() else "cpu"
    )

    model = GeneralizedGRU(
        input_size=24,
        hidden_size=128,
        num_layers=1
    )

    model = model.to(device)

    print("\nDevice:", device)

    print("\nModel Created Successfully.")

    print(model)

   

    total_parameters = sum(
        p.numel()
        for p in model.parameters()
    )

    trainable_parameters = sum(
        p.numel()
        for p in model.parameters()
        if p.requires_grad
    )

    print()

    print("Total Parameters :", total_parameters)

    print("Trainable Parameters :", trainable_parameters)

    # -----------------------
    # Loss Function
    # -----------------------

    criterion = nn.MSELoss()

    print()

    print("Loss Function")

    print(criterion)


    # -----------------------
    # Optimizer
    # -----------------------

    optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001,
    weight_decay=1e-4
    )

    print()

    print("Optimizer")

    print(optimizer)



    scheduler = ReduceLROnPlateau(
    optimizer,
    mode="min",
    factor=0.5,
    patience=2
    )

    print()

    print("Scheduler")

    print(scheduler)


    print()
    train_loss_history = []

    validation_loss_history = []

    best_validation_loss = float("inf")

    patience = 5

    early_stop_counter = 0


    num_epochs = 20

    for epoch in range(num_epochs):

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

      scheduler.step(validation_loss)

      train_loss_history.append(train_loss)

      validation_loss_history.append(validation_loss)

      print()

      print(f"Epoch {epoch + 1}/{num_epochs}")

      print(f"Training Loss   : {train_loss:.6f}")

      print(f"Validation Loss : {validation_loss:.6f}")

      print(
        f"Learning Rate   : "
        f"{optimizer.param_groups[0]['lr']:.6f}"
      )
      # -----------------------
      # Save Best Model
      # -----------------------

      if validation_loss < best_validation_loss:

         best_validation_loss = validation_loss

         os.makedirs(
        "models/version2",
        exist_ok=True
         )

         torch.save(
        model.state_dict(),
        "models/version2/best_generalized_gru.pth"
    )

         print("Best model saved.")

         early_stop_counter = 0

      else:

         early_stop_counter += 1



      # -----------------------
      # Early Stopping
      # -----------------------

      if early_stop_counter >= patience:

         print()

         print("Early stopping triggered.")

         break
      



    
    os.makedirs(
    "results/version2",
    exist_ok=True
    )

    history = {
    "train_loss": train_loss_history,
    "validation_loss": validation_loss_history
   }

    joblib.dump(
    history,
    "results/version2/training_history.pkl"
    )

   
   

    model = load_best_model(
    model,
    "models/version2/best_generalized_gru.pth",
    device
)
    print()
    print("Best model loaded.")
    print()

    print("Training history saved.")

    print()

    print("Training History")

    print()

    print("Training Losses")

    print(train_loss_history)

    print()

    print("Validation Losses")

    print(validation_loss_history)

   

    plt.figure(figsize=(8,5))

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

    plt.title("Version 2 Generalized GRU")

    plt.legend()

    plt.grid(True)


    plt.savefig(
    "results/version2/training_loss.png",
    dpi=300,
    bbox_inches="tight"
   )

    print()

    print("Training curve saved.")
    plt.show()



    print()

    print("=" * 60)
    print("TRAINING COMPLETE")
    print("=" * 60)

    print(f"Best Validation Loss : {best_validation_loss:.6f}")

    print(
    "Model Saved At : "
    "models/version2/best_generalized_gru.pth"
    )

    print(
    "History Saved At : "
    "results/version2/training_history.pkl"
    )

    print(
    "Plot Saved At : "
    "results/version2/training_loss.png"
    )
    


if __name__ == "__main__":
    main()