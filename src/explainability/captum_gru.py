"""
captum_gru.py

Purpose:
Generate feature attribution
for the trained GRU model
using Captum Integrated Gradients.
"""

import numpy as np
import torch
import pandas as pd
import os
import matplotlib.pyplot as plt

from captum.attr import IntegratedGradients

from src.models.gru_model import GRUModel



def main():

    print("=" * 60)
    print("GRU EXPLAINABILITY USING CAPTUM")
    print("=" * 60)

    # ---------------------------------
    # Device
    # ---------------------------------

    device = torch.device(
        "cuda"
        if torch.cuda.is_available()
        else "cpu"
    )




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

    print(f"\nDevice: {device}")



    # ---------------------------------
    # Load Test Data
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
    # Select Samples to Explain
    # ---------------------------------

    explain_data = X_test[:100]

    print("\nExplain Dataset")
    print("Explain Shape :", explain_data.shape)
   


     
    # ---------------------------------
    # Initialize Integrated Gradients
    # ---------------------------------

    ig = IntegratedGradients(model)

    print("\nIntegrated Gradients Initialized Successfully.")




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





    # ---------------------------------
    # Compute Attribution (One Sample)
    # ---------------------------------
    #attributions = ig.attribute(
    #    explain_data[0].unsqueeze(0),
    #    target=0
    #)
    #print("\nAttributions Computed Successfully.")
    #print("Attribution Shape :")
    #print(attributions.shape)




    # ---------------------------------
    # Compute Attributions
    # ---------------------------------

    attributions = ig.attribute(
        explain_data
    )

    print("\nAttributions Computed Successfully.")

    print("Attribution Shape :")
    print(attributions.shape)





    # ---------------------------------
    # Attribution Summary
    # ---------------------------------

    print("\nAttribution Summary")

    print(
        f"Minimum : {attributions.min().item():.6f}"
    )

    print(
        f"Maximum : {attributions.max().item():.6f}"
    )

    print(
        f"Mean    : {attributions.mean().item():.6f}"
    )






    # ---------------------------------
    # Average Absolute Attribution
    # ---------------------------------

    average_importance = (
        attributions
        .abs()
        .mean(dim=0)
    )

    print("\nAverage Importance Shape :")
    print(average_importance.shape)





    # ---------------------------------
    # Sensor Importance
    # ---------------------------------

    sensor_importance = average_importance.mean(dim=0)

    print("\nSensor Importance Shape :")
    print(sensor_importance.shape)

    print("\nSensor Importance Values")

    print(sensor_importance)




     # ---------------------------------
     # Feature Names
     # ---------------------------------

    feature_names = [
    "op_setting_1",
    "op_setting_2",
    "sensor_2",
    "sensor_3",
    "sensor_4",
    "sensor_6",
    "sensor_7",
    "sensor_8",
    "sensor_9",
    "sensor_11",
    "sensor_12",
    "sensor_13",
    "sensor_14",
    "sensor_15",
    "sensor_17",
    "sensor_20",
    "sensor_21"
     ]

    print("\nFeature Names")

    print(feature_names)





    # ---------------------------------
    # Feature Importance DataFrame
    # ---------------------------------
    importance_df = pd.DataFrame(
    {
        "Feature": feature_names,
        "Importance": sensor_importance.cpu().numpy()
    }
    )
   
    print("\nSensor Importance DataFrame")

    print(importance_df.head())




    # ---------------------------------
    # Sort Feature Importance
    # ---------------------------------

    importance_df = importance_df.sort_values(
        by="Importance",
        ascending=False
    ).reset_index(drop=True)

    # to prevent printing all 17 sensors
    #print("\nTop Sensors")
    #print(importance_df)

    print("\nTop 10 Most Important Features")
    print(importance_df.head(10))



    # ---------------------------------
    # Save Feature Importance
    # ---------------------------------

    os.makedirs(
        "results",
        exist_ok=True
    )

    importance_df.to_csv(
        "results/captum_sensor_importance.csv",
        index=False
    )

    importance_df.head(10).to_csv(
    "results/top10_gru_sensors.csv",
    index=False
    
    )

    print(
    "Top 10 sensor importance saved successfully."
    )

    print(
        "\nSensor importance saved successfully."
    )






    # ---------------------------------
    # Feature Importance Plot
    # ---------------------------------

    plt.figure(figsize=(10, 6))

    plt.barh(
        importance_df["Feature"],
        importance_df["Importance"]
    )

    plt.title(
        "GRU Feature Importance using Integrated Gradients"
    )

    plt.xlabel("Importance Score")

    plt.ylabel("Sensors")

    plt.gca().invert_yaxis()

    os.makedirs(
        "results/plots",
        exist_ok=True
    )

    plt.tight_layout()

    plt.savefig(
        "results/plots/gru_feature_importance.png",
        dpi=300
    )

    plt.close()

    print(
        "\nFeature Importance Plot Saved Successfully."
    )



    
    # ---------------------------------
    # Average Attribution Heatmap Data
    # ---------------------------------

    heatmap_data = (
        attributions
        .abs()
        .mean(dim=0)
        .cpu()
        .numpy()
    )

    print("\nHeatmap Shape :")
    print(heatmap_data.shape)




    # ---------------------------------
    # Attribution Heatmap
    # ---------------------------------

    plt.figure(figsize=(10, 8))

    plt.imshow(
        heatmap_data,
        aspect="auto",
        cmap="viridis"
    )

    plt.colorbar(
        label="Attribution Importance"
    )

    plt.title(
        "GRU Attribution Heatmap"
    )

    plt.xlabel("Features")

    plt.ylabel("Time Step")

    plt.xticks(
        ticks=np.arange(len(feature_names)),
        labels=feature_names,
        rotation=90
    )

    plt.tight_layout()

    plt.savefig(
        "results/plots/gru_attribution_heatmap.png",
        dpi=300
    )

    plt.close()

    print(
        "\nAttribution Heatmap Saved Successfully."
    )





    # ---------------------------------
    # Select One Engine
    # ---------------------------------

    engine_sample = explain_data[0].unsqueeze(0)

    print("\nSelected Engine Shape:")

    print(engine_sample.shape)



    # ---------------------------------
    # Predict Selected Engine
    # ---------------------------------

    with torch.no_grad():

        prediction = model(engine_sample)

    print("\nPredicted RUL")

    print(prediction.item())




    # ---------------------------------
    # Save Prediction
    # ---------------------------------

    prediction_df = pd.DataFrame(
        {
            "Predicted_RUL": [
                prediction.item()
            ]
        }
    )

    prediction_df.to_csv(
        "results/gru_prediction.csv",
        index=False
    )

    print(
        "\nPrediction saved successfully."
    )



    # ---------------------------------
    # Explain Selected Engine
    # ---------------------------------

    engine_attribution = ig.attribute(
        engine_sample
    )

    print("\nEngine Attribution Shape")

    print(engine_attribution.shape)


    # ---------------------------------
    # Remove Batch Dimension
    # ---------------------------------

    engine_attribution = (
        engine_attribution
        .squeeze(0)
    )

    print("\nEngine Attribution Shape")

    print(engine_attribution.shape)



    # ---------------------------------
    # Feature Importance for Engine
    # ---------------------------------

    engine_feature_importance = (
        engine_attribution
        .abs()
        .mean(dim=0)
    )

    print("\nEngine Feature Importance")

    print(engine_feature_importance.shape)





    # ---------------------------------
    # Engine Feature DataFrame
    # ---------------------------------

    engine_df = pd.DataFrame(
        {
            "Feature": feature_names,
            "Importance": engine_feature_importance.cpu().numpy()
        }
    )

    print("\nEngine Feature Importance")

    print(engine_df)




    # ---------------------------------
    # Rank Engine Features
    # ---------------------------------

    engine_df = engine_df.sort_values(
        by="Importance",
        ascending=False
    ).reset_index(drop=True)

    print("\nTop 5 Features For This Engine")

    print(engine_df.head(5))





    # ---------------------------------
    # Save Engine Explanation
    # ---------------------------------

    engine_df.to_csv(
        "results/gru_engine_explanation.csv",
        index=False
    )

    print(
        "\nEngine explanation saved successfully."
    )





    # ---------------------------------
    # Human Readable Explanation
    # ---------------------------------

    top_features = engine_df["Feature"].head(5).tolist()

    print("\nExplanation")

    print(
        f"The GRU predicted an RUL of {prediction.item():.2f} cycles."
    )

    print(
        "The prediction was mainly influenced by:"
    )

    for i, feature in enumerate(top_features, start=1):

        print(f"{i}. {feature}")



if __name__ == "__main__":
    main()