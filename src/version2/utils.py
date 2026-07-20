import torch
import numpy as np

from src.version2.generalized_gru import (
    GeneralizedGRU
)
from pathlib import Path


def load_model(device):
    """
    Load trained generalized model.
    """
    model = GeneralizedGRU(
    input_size=24,
    hidden_size=128,
    num_layers=1
)
    

    path = Path("models/version2/best_generalized_gru.pth").resolve()
    print("Loading model from:")
    print(path)
    model.load_state_dict(
    
    torch.load(
        "models/version2/best_generalized_gru.pth",
        map_location=device
    )
)
    
    model.to(device)

    model.eval()

    return model