import numpy as np
import os
import torch
import pandas as pd

from captum.attr import IntegratedGradients

import matplotlib.pyplot as plt

from src.version2.generalized_gru import GeneralizedGRU


FEATURE_NAMES = [

    "Operational Setting 1",
    "Operational Setting 2",
    "Operational Setting 3",

    "Sensor 1",
    "Sensor 2",
    "Sensor 3",
    "Sensor 4",
    "Sensor 5",
    "Sensor 6",
    "Sensor 7",
    "Sensor 8",
    "Sensor 9",
    "Sensor 10",
    "Sensor 11",
    "Sensor 12",
    "Sensor 13",
    "Sensor 14",
    "Sensor 15",
    "Sensor 16",
    "Sensor 17",
    "Sensor 18",
    "Sensor 19",
    "Sensor 20",
    "Sensor 21"

]


MODEL_PATH = (
    "models/version2/best_generalized_gru.pth"
)


def load_model(device):
    """
    Load the trained generalized model.
    """

    model = GeneralizedGRU(
        input_size=24,
        hidden_size=128,
        num_layers=1
    )
    model.load_state_dict(
        torch.load(
            MODEL_PATH,
            map_location=device
        )
    )

    model.to(device)

    model.eval()

    return model


BACKGROUND_PATH = (
    "DATA/version2/sequences/FD001_train_X.npy"
)


def load_background_data():
    """
    Load background samples for SHAP.
    """

    background = np.load(
        BACKGROUND_PATH
    )

    background = background[:100]

    background = torch.tensor(
        background,
        dtype=torch.float32
    )

    return background

def create_integrated_gradients(
    model
):
    """
    Create Captum Integrated Gradients.
    """
    ig = IntegratedGradients(model)

    return ig


def load_sample():
    """
    Load one sample for explanation.
    """

    X = np.load(
        "DATA/version2/sequences/FD001_test_X.npy"
    )

    sample = X[:1]

    sample = torch.tensor(
        sample,
        dtype=torch.float32
    )

    return sample



def compute_feature_attributions(
    ig,
    sample
):
    """
    Compute Integrated Gradients.
    """

    baseline = torch.zeros_like(sample)

    attributions = ig.attribute(
        sample,
        baselines=baseline
    )

    return attributions


def aggregate_feature_importance(
    attributions
):
    """
    Aggregate feature importance across
    all timesteps.
    """

    importance = (
        attributions
        .detach()
        .cpu()
        .numpy()
    )

    importance = importance[0]

    importance = np.mean(
        np.abs(importance),
        axis=0
    )

    return importance






def create_importance_dataframe(
    importance
):
    """
    Create feature importance dataframe.
    """

    df = pd.DataFrame(
        {
            "Feature": FEATURE_NAMES,
            "Importance": importance
        }
    )

    df = df.sort_values(
        by="Importance",
        ascending=False
    )

    df = df.reset_index(
        drop=True
    )

    return df






def plot_feature_importance(
    importance_df
):
    """
    Plot feature importance.
    """

    plt.figure(
        figsize=(10,8)
    )

    plt.barh(
        importance_df["Feature"],
        importance_df["Importance"]
    )

    plt.gca().invert_yaxis()

    plt.xlabel(
        "Importance Score"
    )

    plt.ylabel(
        "Features"
    )

    plt.title(
        "Integrated Gradients Feature Importance"
    )

    plt.grid(
        axis="x"
    )

    plt.tight_layout()

    plt.savefig(
        "results/version2/feature_importance.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()









def generate_attributions(model, sample):
    """
    Generate feature importance for one prediction.

    Parameters
    ----------
    model : torch.nn.Module
        Trained Version 2 GRU model.

    sample : torch.Tensor
        Input sequence of shape
        (1, sequence_length, features).

    Returns
    -------
    list
        Feature importance sorted from
        highest to lowest.
    """

    model.eval()

    ig = create_integrated_gradients(model)

    attributions = compute_feature_attributions(
        ig,
        sample
    )

    importance = aggregate_feature_importance(
        attributions
    )

    importance_df = create_importance_dataframe(
        importance
    )

    return [
        {
            "feature": row["Feature"],
            "importance": round(
                float(row["Importance"]),
                6
            ),
        }
        for _, row in importance_df.iterrows()
    ]


def main():

    print()

    print("=" * 60)

    print("GENERALIZED SHAP EXPLAINABILITY")

    print("=" * 60)

    device = torch.device(
        "cuda"
        if torch.cuda.is_available()
        else "cpu"
    )

    print()

    print("Device:", device)


    model = load_model(device)

    print()

    print("Model Loaded Successfully")

    background = load_background_data()

    background = background.to(device)

    print()

    print(
        "Background Shape:",
        background.shape
    )

    sample = load_sample()

    sample = sample.to(device)

    print()

    print(
        "Sample Shape:",
        sample.shape
    )

    ig = create_integrated_gradients(
    model
)

    print()

    print("Integrated Gradients Ready")


    attributions = compute_feature_attributions(
    ig,
    sample
)
    


    print()

    print("Attributions Computed")

    print()

    print(
    "Attribution Shape:",
    attributions.shape
)
    
    importance = aggregate_feature_importance(
    attributions
)
    print()

    print(
    "Feature Importance Shape:",
    importance.shape
) 
    
    print()

    print(
    "First Five Importances"
)

    print(
    importance[:5]
)
    
    importance_df = create_importance_dataframe(
    importance
)
    print()

    print("="*60)

    print("FEATURE IMPORTANCE")

    print("="*60)

    print()

    print(importance_df)
    importance_df.to_csv(
    "results/version2/feature_importance.csv",
    index=False
)
    print()

    print(
    "Feature importance saved."
)
    
    plot_feature_importance(
    importance_df
)


    


if __name__ == "__main__":
    main()