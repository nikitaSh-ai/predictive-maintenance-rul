import torch
import numpy as np

from src.version2.generalized_gru import (
    GeneralizedGRU
)



from src.version2.utils import load_model




def load_sample():
    """
    Load one test sample.
    """

    X = np.load(
    "DATA/version2/sequences/FD001_test_X.npy"
)

    return torch.FloatTensor(
        X[:1]
    )




def enable_dropout(model):
    """
    Enable dropout during inference.
    """

    for module in model.modules():

        if isinstance(
            module,
            torch.nn.Dropout
        ):

            module.train()




def monte_carlo_prediction(
    model,
    sample,
    passes=50
):
    """
    Monte Carlo Dropout prediction.
    """

    enable_dropout(model)

    predictions = []

    for _ in range(passes):

        prediction = model(sample)

        predictions.append(
            prediction.item()
        )

    predictions = np.array(
        predictions
    )

    mean_prediction = np.mean(
        predictions
    )

    std_prediction = np.std(
        predictions
    )

    return (
        mean_prediction,
        std_prediction,
        predictions
    )





def generate_decision(
    predicted_rul,
    uncertainty
):
    """
    Generate maintenance recommendation.
    """

    if predicted_rul <= 20:

        return {

            "priority": "Critical",

            "recommendation":
            "Immediate Maintenance Required",

            "inspection":
            "Stop engine and inspect immediately.",

            "focus":
            "Critical components",

            "reason":
            (
                "Predicted RUL is critically low."
            ),

            "risk": "Critical"
        }

    elif predicted_rul <= 50:

        return {

            "priority": "High",

            "recommendation":
            "Schedule Maintenance Soon",

            "inspection":
            "Inspect within the next maintenance window.",

            "focus":
            "Engine degradation",

            "reason":
            (
                "Remaining life is limited."
            ),

            "risk": "High"
        }

    elif predicted_rul <= 80:

        return {

            "priority": "Medium",

            "recommendation":
            "Monitor Engine Condition",

            "inspection":
            "Increase monitoring frequency.",

            "focus":
            "Wear trend",

            "reason":
            (
                "Engine is degrading but still operational."
            ),

            "risk": "Medium"
        }

    else:

        return {

            "priority": "Low",

            "recommendation":
            "Engine Healthy",

            "inspection":
            "Routine inspection only.",

            "focus":
            "Normal operation",

            "reason":
            (
                "Predicted RUL indicates healthy condition."
            ),

            "risk": "Low"
        }



def main():

    print()

    print("=" * 60)

    print("GENERALIZED DECISION ENGINE")

    print("=" * 60)

    device = torch.device(
    "cuda"
    if torch.cuda.is_available()
    else "cpu"
)

    print()

    print("Device:", device)

    model = load_model(device)

    sample = load_sample()

    sample = sample.to(device)

    mean_prediction, uncertainty, predictions = (
    monte_carlo_prediction(
        model,
        sample,
        passes=50
    )
)
    
    decision = generate_decision(
    mean_prediction,
    uncertainty
)
    
    print()

    print(
    f"Predicted RUL : {mean_prediction:.2f}"
)
    
    print(
    f"Prediction Uncertainty : "
    f"{uncertainty:.2f}"
)
    
    print()

    print(
    "Maintenance Recommendation"
)

    print(
    "Decision :",
    decision["decision"]
)

    print(
    "Risk Level :",
    decision["risk"]
)





if __name__ == "__main__":
    main()


