import torch
import os
import numpy as np
import matplotlib.pyplot as plt

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
      predictions.append(prediction.item())

        

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








def plot_prediction_distribution(
    predictions,
    mean_prediction,
    uncertainty
):
    """
    Plot Monte Carlo prediction distribution.
    """

    plt.figure(
        figsize=(8,5)
    )

    plt.hist(
        predictions,
        bins=20,
        edgecolor="black"
    )

    plt.axvline(
    mean_prediction,
    color="red",
    linestyle="--",
    linewidth=2,
    label="Mean Prediction"
)
    
    plt.axvline(
    mean_prediction - uncertainty,
    color="green",
    linestyle=":",
    linewidth=2,
    label="-1 Std"
)
    plt.axvline(
    mean_prediction + uncertainty,
    color="green",
    linestyle=":",
    linewidth=2,
    label="+1 Std"
)
    plt.legend()
    

    plt.xlabel(
        "Predicted RUL"
    )

    plt.ylabel(
        "Frequency"
    )

    plt.title(
        "Monte Carlo Prediction Distribution"
    )

    plt.grid(True)

    plt.tight_layout()

    os.makedirs(
    "results/version2",
    exist_ok=True
)

    plt.savefig(
    "results/version2/uncertainty_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

    plt.show()







def main():

    print()

    print("=" * 60)

    print("MONTE CARLO DROPOUT")

    print("=" * 60)

    device = torch.device(
    "cuda"
    if torch.cuda.is_available()
    else "cpu")

    print()

    print("Device:", device)
    model = load_model(
    device
)

    print()

    print("Model Loaded Successfully")

    sample = load_sample()

    sample = sample.to(device)

    print()

    print(
    "Sample Shape:",
    sample.shape
)
    mean_prediction, uncertainty, predictions = (
    monte_carlo_prediction(
        model,
        sample
    )
)
    
    print()

    print("Mean Prediction")

    print(mean_prediction)

    print()

    print("Prediction Uncertainty")

    print(uncertainty)

    print()

    print("First 10 Predictions")

    print(
    predictions[:10]
)
    
    print()

    print("Minimum Prediction")

    print(
    predictions.min()
)
    print()

    print("Maximum Prediction")

    print(
    predictions.max()
)
    plot_prediction_distribution(
    predictions,
    mean_prediction,
    uncertainty
)



if __name__ == "__main__":
    main()