"""
evaluate_model.py

Purpose:
Common evaluation functions for all regression models.
"""

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

import numpy as np


def evaluate_regression(y_true, y_pred):
    """
    Compute regression metrics.
    """

    mae = mean_absolute_error(y_true, y_pred)

    rmse = np.sqrt(
        mean_squared_error(y_true, y_pred)
    )

    r2 = r2_score(y_true, y_pred)

    return {
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2
    }


def print_metrics(metrics, dataset_name):
    """
    Display evaluation metrics.
    """

    print("\n" + "=" * 50)

    print(dataset_name)

    print("=" * 50)

    print(f"MAE  : {metrics['MAE']:.4f}")
    print(f"RMSE : {metrics['RMSE']:.4f}")
    print(f"R²   : {metrics['R2']:.4f}")