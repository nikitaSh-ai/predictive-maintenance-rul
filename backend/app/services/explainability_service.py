import torch

from captum.attr import IntegratedGradients

from backend.app.services.model_service import model

IG = IntegratedGradients(model)

FEATURE_NAMES = [

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
    "sensor_21",

]


LATEST_EXPLANATION = {}



def generate_attributions(input_tensor):
    """
    Generate feature importance using
    Captum Integrated Gradients.
    """

    model.eval()

    

    baseline = torch.zeros_like(input_tensor)

    attributions = IG.attribute(
    input_tensor,
    baselines=baseline,
    n_steps=20
)
    feature_importance = attributions.abs().mean(dim=1).squeeze(0)


    importance_dict = {

    feature: float(score)

    for feature, score in zip(
        FEATURE_NAMES,
        feature_importance
    )

    }

    global LATEST_EXPLANATION

    LATEST_EXPLANATION = importance_dict

    

    return importance_dict
 
