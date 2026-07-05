"""
shap_random_forest.py

Purpose:
Generate SHAP explanations
for the trained Random Forest model.
"""

import joblib
import os
import shap
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from src.models.create_sequences import get_feature_columns


def main():

    print("=" * 60)
    print("RANDOM FOREST SHAP EXPLAINABILITY")
    print("=" * 60)

    # ---------------------------------
    # Load Random Forest Model
    # ---------------------------------

    model = joblib.load(
        "models/random_forest.pkl"
    )

    print(
        "\nRandom Forest model loaded successfully."
    )


    


    # ---------------------------------
    # Load Test Data
    # ---------------------------------

    X_test = np.load(
        "DATA/sequences/X_test.npy"
    )

    y_test = np.load(
        "DATA/sequences/y_test.npy"
    )

    print("\nOriginal Shape")

    print("X_test :", X_test.shape)

    X_test = X_test.reshape(
        X_test.shape[0],
        -1
    )

    print("\nFlattened Shape")

    print("X_test :", X_test.shape)

    print("y_test :", y_test.shape)




    # ---------------------------------
    # Create TreeExplainer
    # ---------------------------------

    explainer = shap.TreeExplainer(
        model
    )

    print(
        "\nSHAP TreeExplainer created successfully."
    )






    # ---------------------------------
    # Select Samples to Explain
    # ---------------------------------

    explain_data = X_test[:100]

    print("\nExplain Data")

    print(explain_data.shape)



    # ---------------------------------
    # Compute SHAP Values
    # ---------------------------------

    shap_values = explainer.shap_values(
    explain_data,
    check_additivity=False
    )

    print(
        "\nSHAP values computed successfully."
    )

    print(
        "SHAP Shape :",
        np.array(shap_values).shape
    )

    print("\nSHAP Statistics")
    print("Maximum :", np.max(shap_values))
    print("Minimum :", np.min(shap_values))
    print("Mean    :", np.mean(shap_values))
    print("Median  :", np.median(shap_values))




    # ---------------------------------
    # Global SHAP Importance
    # ---------------------------------

    global_importance = np.abs(
        shap_values
    ).mean(axis=0)

    print("\nGlobal Importance Shape")

    print(global_importance.shape)




    # ---------------------------------
    # Build Feature Names
    # ---------------------------------

    train_df = pd.read_csv(
        "DATA/processed/train_scaled.csv"
    )

    feature_cols = get_feature_columns(
        train_df
    )

    sequence_length = 40

    feature_names = []

    for t in range(sequence_length):

        for feature in feature_cols:

            feature_names.append(
                f"{feature}_t-{sequence_length-1-t}"
            )

    print("\nNumber of Feature Names")

    print(len(feature_names))





    # ---------------------------------
    # SHAP Importance DataFrame
    # ---------------------------------

    importance_df = pd.DataFrame(
        {
            "Feature": feature_names,
            "Importance": global_importance
        }
    )

    print("\nSHAP Importance DataFrame")

    print(importance_df.head())







    # ---------------------------------
    # Sort SHAP Importance
    # ---------------------------------

    importance_df = importance_df.sort_values(
        by="Importance",
        ascending=False
    ).reset_index(drop=True)

    print("\nTop 10 SHAP Features")

    print(
        importance_df.head(10)
    )





    # ---------------------------------
    # Save SHAP Importance
    # ---------------------------------

    os.makedirs(
        "results",
        exist_ok=True
    )

    importance_df.to_csv(
        "results/random_forest_shap_importance.csv",
        index=False
    )

    importance_df.head(10).to_csv(
        "results/random_forest_top10_shap.csv",
        index=False
    )

    print(
        "\nSHAP importance saved successfully."
    )






    # ---------------------------------
    # SHAP Summary Plot
    # ---------------------------------

    os.makedirs(
        "results/plots",
        exist_ok=True
    )

    plt.figure(figsize=(12, 8))

    shap.summary_plot(
        shap_values,
        explain_data,
        feature_names=feature_names,
        show=False
    )

    plt.tight_layout()

    plt.savefig(
        "results/plots/random_forest_shap_summary.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print(
        "\nSHAP Summary Plot Saved Successfully."
    )



    print("Prediction Range")
    print(model.predict(explain_data).min())
    print(model.predict(explain_data).max())




if __name__ == "__main__":
    main()