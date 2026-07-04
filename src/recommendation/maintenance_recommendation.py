"""
maintenance_recommendation.py

Purpose:
Generate maintenance recommendations
using predicted Remaining Useful Life
and explainability results.
"""

import pandas as pd


def main():

    print("=" * 60)
    print("MAINTENANCE RECOMMENDATION ENGINE")
    print("=" * 60)



    # ---------------------------------
    # Load Explanation
    # ---------------------------------

    explanation_df = pd.read_csv(
        "results/gru_engine_explanation.csv"
    )

    print("\nExplanation Loaded Successfully.")

    print(explanation_df.head())




    # ---------------------------------
    # Load Prediction
    # ---------------------------------

    prediction_df = pd.read_csv(
        "results/gru_prediction.csv"
    )

    print("\nPrediction Loaded Successfully.")

    print(prediction_df)



    # ---------------------------------
    # Extract Prediction
    # ---------------------------------

    predicted_rul = prediction_df.loc[
        0,
        "Predicted_RUL"
    ]

    print("\nPredicted RUL")

    print(predicted_rul)




    # ---------------------------------
    # Risk Classification
    # ---------------------------------

    if predicted_rul > 100:

        risk_level = "Healthy"

    elif predicted_rul > 60:

        risk_level = "Low Risk"

    elif predicted_rul > 30:

        risk_level = "Medium Risk"

    elif predicted_rul > 10:

        risk_level = "High Risk"

    else:

        risk_level = "Critical"

    print("\nRisk Level")

    print(risk_level)





    # ---------------------------------
    # Maintenance Recommendation
    # ---------------------------------

    if risk_level == "Healthy":

        recommendation = (
            "Continue normal operation."
        )

    elif risk_level == "Low Risk":

        recommendation = (
            "Schedule routine inspection."
        )

    elif risk_level == "Medium Risk":

        recommendation = (
            "Plan maintenance soon."
        )

    elif risk_level == "High Risk":

        recommendation = (
            "Prioritize maintenance."
        )

    else:

        recommendation = (
            "Immediate maintenance required."
        )

    print("\nMaintenance Recommendation")

    print(recommendation)



    # ---------------------------------
    # Top 5 Influential Features
    # ---------------------------------

    top_features = (
        explanation_df["Feature"]
        .head(5)
        .tolist()
    )

    print("\nTop Influential Features")

    for feature in top_features:

        print(feature)



    # ---------------------------------
    # Final Maintenance Report
    # ---------------------------------

    print("\n" + "=" * 60)
    print("ENGINE MAINTENANCE REPORT")
    print("=" * 60)

    print(
        f"\nPredicted RUL : {predicted_rul:.2f} cycles"
    )

    print(
        f"Risk Level    : {risk_level}"
    )

    print("\nTop Influencing Features")

    for i, feature in enumerate(
        top_features,
        start=1
    ):

        print(f"{i}. {feature}")

    print("\nRecommendation")

    print(recommendation)




    # ---------------------------------
    # Save Maintenance Report
    # ---------------------------------

    report_df = pd.DataFrame(
        {
            "Predicted_RUL": [predicted_rul],
            "Risk_Level": [risk_level],
            "Recommendation": [recommendation],
            "Top_Feature_1": [top_features[0]],
            "Top_Feature_2": [top_features[1]],
            "Top_Feature_3": [top_features[2]],
            "Top_Feature_4": [top_features[3]],
            "Top_Feature_5": [top_features[4]]
        }
    )

    report_df.to_csv(
        "results/maintenance_report.csv",
        index=False
    )

    print(
        "\nMaintenance report saved successfully."
    )


if __name__ == "__main__":
    main()