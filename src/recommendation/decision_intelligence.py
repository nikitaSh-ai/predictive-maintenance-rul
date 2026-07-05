"""
decision_intelligence.py

Purpose:
Convert AI predictions into
maintenance decisions for engineers.
"""

import pandas as pd
import json

def main():

    print("=" * 60)
    print("DECISION INTELLIGENCE ENGINE")
    print("=" * 60)



    # ---------------------------------
    # File Paths
    # ---------------------------------

    prediction_path = "results/gru_prediction.csv"

    explanation_path = "results/gru_engine_explanation.csv"

    report_path = "results/decision_intelligence_report.csv"


    # ---------------------------------
    # Load Prediction
    # ---------------------------------

    prediction_df = pd.read_csv(
    prediction_path
   )

    print("\nPrediction Loaded Successfully.")

    print(prediction_df.head())




    # ---------------------------------
    # Load Explanation
    # ---------------------------------

    explanation_df = pd.read_csv(
    explanation_path
   )

    print("\nExplanation Loaded Successfully.")

    print(explanation_df.head())




    # ---------------------------------
    # Extract Prediction
    # ---------------------------------

    predicted_rul = float(
    prediction_df.loc[0, "Predicted_RUL"]
    )

    print("\nPredicted RUL")

    print(predicted_rul)


    # ---------------------------------
    # Top Features
    # ---------------------------------

    top_features = explanation_df[
    "Feature"
    ].tolist()

    print("\nTop 5 Features")

    for feature in top_features[:5]:

       print(feature)


    # ---------------------------------
    # Risk Assessment
    # ---------------------------------

    if predicted_rul <= 20:

     risk_level = "Critical"

    elif predicted_rul <= 50:

     risk_level = "High"

    elif predicted_rul <= 80:

     risk_level = "Medium"

    else:

     risk_level = "Low"

    print("\nRisk Level")

    print(risk_level)


    # ---------------------------------
    # Maintenance Priority
    # ---------------------------------

    if risk_level == "Critical":

     priority = "Immediate"

    elif risk_level == "High":

     priority = "Urgent"

    elif risk_level == "Medium":

     priority = "Scheduled"

    else:

     priority = "Routine"

    print("\nMaintenance Priority")

    print(priority)




    # ---------------------------------
    # Maintenance Action
    # ---------------------------------

    if risk_level == "Critical":

     action = "Shut down the engine immediately."

    elif risk_level == "High":

     action = "Perform maintenance as soon as possible."

    elif risk_level == "Medium":

     action = "Schedule maintenance during the next maintenance window."

    else:

     action = "Continue normal operation."

    print("\nMaintenance Action")

    print(action)



    # ---------------------------------
    # Inspection Targets
    # ---------------------------------

    inspection_targets = top_features[:3]

    print("\nInspection Targets")

    for i, sensor in enumerate(
    inspection_targets,
    start=1
    ):
     print(f"{i}. {sensor}")







    # ---------------------------------
    # AI Reasoning
    # ---------------------------------

    reason = (
    "The recommendation is based on the "
    "predicted Remaining Useful Life and "
    "the three most influential features "
    "identified using Captum Integrated Gradients."
     )

    print("\nAI Reasoning")

    print(reason)
    



    # ---------------------------------
    # Maintenance Window
    # ---------------------------------

    if predicted_rul <= 10:

     maintenance_window = (
        "Immediate maintenance required."
    )

    elif predicted_rul <= 30:

     maintenance_window = (
        f"Schedule maintenance within {int(predicted_rul)} operating cycles."
    )

    elif predicted_rul <= 60:

     maintenance_window = (
        f"Plan maintenance within the next {int(predicted_rul)} operating cycles."
    )

    else:

     maintenance_window = (
        f"No immediate maintenance required. Approximately {int(predicted_rul)} operating cycles remain."
    )

    print("\nEstimated Maintenance Window")

    print(maintenance_window)



    # ---------------------------------
    # AI Decision Report
    # ---------------------------------

    print("\n" + "=" * 60)
    print("AI DECISION REPORT")
    print("=" * 60)

    print(f"Predicted RUL        : {predicted_rul:.2f} cycles")

    print(f"Risk Level           : {risk_level}")

    print(f"Maintenance Priority : {priority}")

    print("\nMaintenance Action")

    print(action)

    print("\nInspection Targets")

    for i, sensor in enumerate(
    inspection_targets,
    start=1
    ):
      print(f"{i}. {sensor}")

    print("\nMaintenance Window")

    print(maintenance_window)

    print("\nReason")

    print(reason)    







    # ---------------------------------
    # Build Decision Report
    # ---------------------------------

    decision_report = {

    "Predicted_RUL": round(predicted_rul, 2),

    "Risk_Level": risk_level,

    "Maintenance_Priority": priority,

    "Maintenance_Action": action,

    "Maintenance_Window": maintenance_window,

    "Inspection_Target_1": inspection_targets[0],

    "Inspection_Target_2": inspection_targets[1],

    "Inspection_Target_3": inspection_targets[2],

    "Reason": reason

    }


    # ---------------------------------
    # Save CSV Report
    # ---------------------------------

    report_df = pd.DataFrame(
    [decision_report]
    )

    report_df.to_csv(
    report_path,
    index=False
    )

    print("\nDecision report saved successfully.")







    # ---------------------------------
    # Save JSON Report
    # ---------------------------------

    with open(
    "results/decision_intelligence_report.json",
    "w"
    ) as f:

      json.dump(
        decision_report,
        f,
        indent=4
       )

    print("Decision report JSON saved successfully.")


    



if __name__ == "__main__":
    main()