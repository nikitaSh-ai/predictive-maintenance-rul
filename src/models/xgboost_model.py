"""
xgboost_model.py

Purpose:
Train an XGBoost baseline model.
"""

import os
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from xgboost import XGBRegressor

from src.models.evaluate_model import (
    evaluate_regression,
    print_metrics
)
from src.models.create_sequences import get_feature_columns





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



def flatten_sequences(X):
    """
    Convert 3D sequences into 2D feature vectors.
    """

    return X.reshape(X.shape[0], -1)

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
    print("XGBOOST DATA")
    print("=" * 60)

    print("\nOriginal Shapes")

    print("Train:", X_train.shape)
    print("Validation:", X_validation.shape)
    print("Test:", X_test.shape)

    X_train = flatten_sequences(X_train)
    X_validation = flatten_sequences(X_validation)
    X_test = flatten_sequences(X_test)

    print("\nFlattened Shapes")

    print("Train:", X_train.shape)
    print("Validation:", X_validation.shape)
    print("Test:", X_test.shape)



    print("\nTraining XGBoost...")

    xgb = XGBRegressor(
        n_estimators=100,
        max_depth=6,
        learning_rate=0.1,
        random_state=42,
        n_jobs=-1
    )

    xgb.fit(X_train, y_train)

    print("Training Complete.")




    print("\nGenerating Predictions...")

    train_pred = xgb.predict(X_train)
    validation_pred = xgb.predict(X_validation)
    test_pred = xgb.predict(X_test)

    print("Prediction Complete.")

    print("\nPrediction Shapes")

    print("Train      :", train_pred.shape)
    print("Validation :", validation_pred.shape)
    print("Test       :", test_pred.shape)



    # -----------------------
    # Evaluate Validation Set
    # -----------------------

    validation_metrics = evaluate_regression(
    y_validation,
    validation_pred
    )

    print_metrics(
    validation_metrics,
    "Validation Metrics"
    )





    # -----------------------
    # Evaluate Test Set
    # -----------------------

    test_metrics = evaluate_regression(
    y_test,
    test_pred
    )

    print_metrics(
    test_metrics,
    "Test Metrics"
    )



    # -----------------------
    # Save trained model
    # -----------------------

    os.makedirs("models", exist_ok=True)

    joblib.dump(
    xgb,
    "models/xgboost.pkl"
    )

    print("\nXGBoost model saved successfully.")





    # -----------------------
    # Save metrics
    # -----------------------

    os.makedirs("results", exist_ok=True)

    with open("results/xgboost_metrics.txt", "w") as f:

      f.write("Validation Metrics\n")
      f.write("=" * 30 + "\n")
      f.write(f"MAE  : {validation_metrics['MAE']:.4f}\n")
      f.write(f"RMSE : {validation_metrics['RMSE']:.4f}\n")
      f.write(f"R2   : {validation_metrics['R2']:.4f}\n\n")

      f.write("Test Metrics\n")
      f.write("=" * 30 + "\n")
      f.write(f"MAE  : {test_metrics['MAE']:.4f}\n")
      f.write(f"RMSE : {test_metrics['RMSE']:.4f}\n")
      f.write(f"R2   : {test_metrics['R2']:.4f}\n")

    print("Metrics saved successfully.")





    # -----------------------
   # Save predictions
   # -----------------------

    validation_results = pd.DataFrame({
    "Actual_RUL": y_validation,
    "Predicted_RUL": validation_pred
    })

    test_results = pd.DataFrame({
    "Actual_RUL": y_test,
    "Predicted_RUL": test_pred
      })

    validation_results.to_csv(
    "results/xgboost_validation_predictions.csv",
    index=False
     )

    test_results.to_csv(
    "results/xgboost_test_predictions.csv",
    index=False
    )

    print("Predictions saved successfully.")








    # -----------------------
    # Prediction vs Actual Plot
    # -----------------------

    plt.figure(figsize=(8, 8))

    plt.scatter(
    y_test,
    test_pred,
    alpha=0.5
    )

    plt.plot(
    [0, 125],
    [0, 125],
    "r--",
    linewidth=2
    )

    plt.xlabel("Actual RUL")
    plt.ylabel("Predicted RUL")
    plt.title("XGBoost: Prediction vs Actual")

    plt.savefig(
    "results/xgboost_prediction_vs_actual.png",
    dpi=300,
    bbox_inches="tight"
    )

    plt.close()

    print("Prediction vs Actual plot saved.")








    # -----------------------
    # Residual Plot
    # -----------------------

    residuals = y_test - test_pred

    plt.figure(figsize=(8, 6))

    plt.scatter(
    test_pred,
    residuals,
    alpha=0.5
    )

    plt.axhline(
    y=0,
    color="red",
    linestyle="--",
    linewidth=2
    )

    plt.xlabel("Predicted RUL")
    plt.ylabel("Residual (Actual - Predicted)")
    plt.title("XGBoost: Residual Plot")

    plt.savefig(
    "results/xgboost_residual_plot.png",
    dpi=300,
    bbox_inches="tight"
    )

    plt.close()

    print("Residual plot saved.")




    # -----------------------
    # Load feature names
    # -----------------------

    train_df = pd.read_csv("DATA/processed/train_scaled.csv")
    feature_cols = get_feature_columns(train_df)



    feature_names = []

    num_features = len(feature_cols)
    sequence_length = X_train.shape[1] // num_features

    for t in range(sequence_length):
      for feature in feature_cols:
        feature_names.append(
            f"{feature}_t-{sequence_length-1-t}"
        )




    # ----------------------------------
    # create and save the dataframe
    # ----------------------------------
    importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": xgb.feature_importances_
    })

    importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
    )

    importance_df.to_csv(
    "results/xgboost_feature_importance.csv",
    index=False
    )

    print("Feature importance saved successfully.")




    # -----------------------
    # Top 20 Feature Importance Plot
    # -----------------------

    top_k = 20
    top_features = importance_df.head(top_k)

    plt.figure(figsize=(10, 8))

    plt.barh(
    top_features["Feature"][::-1],
    top_features["Importance"][::-1]
    )

    plt.xlabel("Importance")
    plt.ylabel("Feature (Time Step)")
    plt.title(f"XGBoost: Top {top_k} Feature Importances")

    plt.gca().invert_yaxis()

    plt.grid(
    axis="x",
    linestyle="--",
    alpha=0.5
    )

    plt.tight_layout()

    plt.savefig(
    "results/xgboost_feature_importance.png",
    dpi=300,
    bbox_inches="tight"
    )

    plt.close()

    print(f"Top {top_k} feature importance plot saved.")

if __name__ == "__main__":
    main()