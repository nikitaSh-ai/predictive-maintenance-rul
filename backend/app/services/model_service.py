from pathlib import Path

import torch

from src.models.gru_model import GRUModel

MODEL_DIR = Path(__file__).resolve().parents[3] / "models"
MODEL_PATH = MODEL_DIR / "best_gru.pth"   # or best_gru_model.pth if you rename it

model = GRUModel(
    input_size=17,
    hidden_size=128,
    num_layers=1,
)

checkpoint = torch.load(
    MODEL_PATH,
    map_location="cpu",
)

model.load_state_dict(checkpoint)

model.eval()

print("GRU model loaded successfully.")


def get_model():
    """
    Return the loaded GRU model.
    """

    return model