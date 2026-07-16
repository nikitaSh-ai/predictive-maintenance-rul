"""
uncertainty.py

Monte Carlo Dropout
for prediction uncertainty.
"""

import numpy as np
import torch



def monte_carlo_prediction(
    model,
    input_tensor,
    num_samples=30
):
    """
    Perform Monte Carlo Dropout prediction.
    """

    predictions = []

    model.train()

    with torch.no_grad():

        for _ in range(num_samples):

            output = model(input_tensor)

            predictions.append(
                output.item()
            )

    mean_prediction = np.mean(predictions)

    std_prediction = np.std(predictions)

    return {

    "mean": round(float(mean_prediction), 2),

    "std": round(float(std_prediction), 2),

    "samples": predictions

    }