"""
decision_intelligence.py

Purpose:
Convert AI predictions into
maintenance decisions for engineers.
"""

import pandas as pd
import json





def main():

    uncertainty_path = "results/uncertainty_results.csv"

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
    # Load Uncertainty
    # ---------------------------------

    uncertainty_df = pd.read_csv(  "results/gru_uncertainty_results.csv"
    )

    print("\nUncertainty Loaded Successfully.")

    print(uncertainty_df.head())


    # ---------------------------------
    # Extract Uncertainty
    # ---------------------------------

    prediction_uncertainty = float(
    uncertainty_df.loc[0, "Uncertainty"]
    )

    print("\nPrediction Uncertainty")

    print(f"{prediction_uncertainty:.2f}")




    # ---------------------------------
    # Prediction Interval
    # ---------------------------------

    lower_bound = float(
    uncertainty_df.loc[0, "Lower_Bound"]
)

    upper_bound = float(
    uncertainty_df.loc[0, "Upper_Bound"]
)

    print("\nPrediction Interval")

    print(f"{lower_bound:.2f} to {upper_bound:.2f} cycles")


    # ---------------------------------
    # Decision Confidence
    # ---------------------------------

    if prediction_uncertainty <= 5:

     decision_confidence = "High"

    elif prediction_uncertainty <= 10:

     decision_confidence = "Medium"

    else:

     decision_confidence = "Low"

    print("\nDecision Confidence")

    print(decision_confidence)




    # ---------------------------------
    # Extract Prediction
    # ---------------------------------

    predicted_rul = float(
    prediction_df.loc[0, "Predicted_RUL"]
    )

    print("\nPredicted RUL")

    print(
    f"{predicted_rul:.2f} ± {prediction_uncertainty:.2f} cycles"
)


    # ---------------------------------
    # Health Score
    # ---------------------------------

    MAX_RUL = 125

    health_score = (
    predicted_rul / MAX_RUL
    ) * 100

    health_score = min(
    health_score,
    100
    )

    print("\nHealth Score")

    print(f"{health_score:.2f}%")


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
    f"The engine is classified as {risk_level.lower()} risk "
    f"with a predicted remaining useful life of "
    f"{predicted_rul:.0f} cycles. "
    f"The recommendation focuses on "
    f"{inspection_targets[0]}, "
    f"{inspection_targets[1]} and "
    f"{inspection_targets[2]} because they were identified as the "
    f"most influential features by Captum Integrated Gradients."
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

    print(
    f"Prediction Interval : "
    f"{lower_bound:.2f} - {upper_bound:.2f} cycles"
    )

    print(
    f"Prediction Uncertainty : "
    f"±{prediction_uncertainty:.2f} cycles"
     )

    print(f"Health Score         : {health_score:.2f}%")

    print(
    f"Decision Confidence : {decision_confidence}"
)

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
    print("\nInspection Guidance : ")
    print("The sensors listed above contributed most strongly to the predicted Remaining Useful Life. Prioritize inspection of these sensors during the next scheduled maintenance activity and compare their readings with historical operating trends before making maintenance decisions.")

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

    "Reason": reason,

    "Prediction_Uncertainty": round(prediction_uncertainty,2),

    "Decision_Confidence": decision_confidence,

    "Prediction_Uncertainty": round(
    prediction_uncertainty,
    2
    ),

    "Lower_Bound": round(
    lower_bound,
    2
    ),

    "Upper_Bound": round(
    upper_bound,
    2
    ),

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