"""
save_gru_predictions.py

Purpose:
Generate predictions using the trained
GRU model and save them to a CSV file.
"""

import os
import numpy as np
import pandas as pd
import torch

from torch.utils.data import TensorDataset, DataLoader

from src.models.gru_model import GRUModel



# ---------------------------------
# Load Test Data
# ---------------------------------

X_test = np.load(
    "DATA/sequences/X_test.npy"
)

y_test = np.load(
    "DATA/sequences/y_test.npy"
)

print("Test Data Loaded")
print("X_test :", X_test.shape)
print("y_test :", y_test.shape)