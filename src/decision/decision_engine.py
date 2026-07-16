"""
decision_engine.py

Business decision engine for
maintenance recommendation.
"""



def generate_decision(
    risk,
    uncertainty
):
    """
    Generate maintenance decision
    based on risk level.
    """

    print("\nDecision Engine")

    print(f"Risk        : {risk}")

    print(f"Uncertainty : {uncertainty:.2f}")

    if risk == "Critical":
        if uncertainty > 3:
           recommendation = (
            "Immediate maintenance required. "
            "Model uncertainty is high. "
            "Perform manual inspection before maintenance."
           )

        else:

          recommendation = (
            "Immediate maintenance required."
        )

        inspection = (
            "Inspect immediately"
        )

        focus = (
            "Immediate maintenance"
        )

        priority = "P1"

        reason = ("Remaining Useful Life is critically low.")

    elif risk == "High":

        if uncertainty > 3:

            recommendation = (
            "Schedule maintenance soon. "
            "Prediction uncertainty is high. "
            "Increase monitoring frequency."
            )

        else:

            recommendation = (
            "Schedule maintenance as soon as possible."
           )

        inspection = (
            "Inspect within 10 cycles"
        )

        focus = (
            "Monitor degradation"
        )

        priority = "P2"

        reason = ("Engine is approaching failure.")

    elif risk == "Medium":
        if uncertainty > 3:

           recommendation = (
            "Plan maintenance. "
            "Prediction uncertainty is elevated. "
            "Inspect before the next maintenance window."
           )

        else:

          recommendation = (
            "Plan maintenance in upcoming cycles."
        )

        inspection = (
            "Inspect within 30 cycles"
        )

        focus = (
            "Routine monitoring"
        )
        priority = "P3"

        reason = ("Engine health is degrading.")

    else:

        recommendation = (
            "Continue normal operation."
        )

        inspection = (
            "Routine inspection"
        )

        focus = (
            "Routine monitoring"
        )
        priority = "P4"

        reason = ("Engine is operating normally.")

    return {

    "priority": priority,

    "recommendation": recommendation,

    "inspection": inspection,

    "focus": focus,

    "reason": reason

}