"""
verify_sequences.py

Purpose:
Verify that generated sequences are correct before
training machine learning models.
"""

import numpy as np

print("=" * 60)
print("SEQUENCE VERIFICATION")
print("=" * 60)

# -----------------------
# Load sequences
# -----------------------
X_train = np.load("DATA/sequences/X_train.npy")
y_train = np.load("DATA/sequences/y_train.npy")

X_validation = np.load("DATA/sequences/X_validation.npy")
y_validation = np.load("DATA/sequences/y_validation.npy")

X_test = np.load("DATA/sequences/X_test.npy")
y_test = np.load("DATA/sequences/y_test.npy")

# -----------------------
# Shapes
# -----------------------
print("\nDataset Shapes")

print("X_train      :", X_train.shape)
print("y_train      :", y_train.shape)

print("X_validation :", X_validation.shape)
print("y_validation :", y_validation.shape)

print("X_test       :", X_test.shape)
print("y_test       :", y_test.shape)

# -----------------------
# Sequence dimensions
# -----------------------
print("\nSequence Length :", X_train.shape[1])
print("Feature Count   :", X_train.shape[2])

# -----------------------
# NaN check
# -----------------------
print("\nNaN Check")

print("X_train :", np.isnan(X_train).sum())
print("y_train :", np.isnan(y_train).sum())

print("X_validation :", np.isnan(X_validation).sum())
print("y_validation :", np.isnan(y_validation).sum())

print("X_test :", np.isnan(X_test).sum())
print("y_test :", np.isnan(y_test).sum())

# -----------------------
# Target statistics
# -----------------------
print("\nTarget Statistics")

print("Minimum RUL :", y_train.min())
print("Maximum RUL :", y_train.max())

print("\nVerification Complete.")