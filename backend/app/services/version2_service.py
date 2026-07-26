import torch
import numpy as np

from src.version2.generalized_gru import (
    GeneralizedGRU
)
from src.version2.generalized_decision_engine import (
    generate_decision
)

from src.version2.uncertainty_estimation import (
    monte_carlo_prediction,
    enable_dropout
)


def load_version2_model():
    """
    Load Version 2 GRU model.
    """
    model = GeneralizedGRU(
    input_size=24,
    hidden_size=128,
    num_layers=1
)
    

    
    model.load_state_dict(
        torch.load(
            "models/version2/best_generalized_gru.pth",
            map_location="cpu"
        )
    )
    model.eval()

    return model




MODEL = load_version2_model()

def predict_rul(
    sequence
):
    """
    Predict RUL using Version 2 model.
    """

    tensor = torch.FloatTensor(
        sequence
    ).unsqueeze(0)

    with torch.no_grad():

        prediction = MODEL(
            tensor
        )

    return prediction.item()



def predict_with_uncertainty(
    sequence
):
    """
    Predict RUL with uncertainty.
    """
    tensor = torch.FloatTensor(sequence).unsqueeze(0)

   

    MODEL.eval()

    

    mean_prediction, uncertainty, samples = monte_carlo_prediction(
        MODEL,
        tensor,
        passes=50
    )

    

    decision = generate_decision(
        mean_prediction,
        uncertainty
    )

    return {
        "predicted_rul": mean_prediction,
        "uncertainty": uncertainty,
        "mc_samples": [float(value) for value in samples],
        "decision": decision,
    }