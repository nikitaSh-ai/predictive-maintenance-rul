import torch
import numpy as np

from src.version2.generalized_gru import GeneralizedGRU

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

X = np.load("DATA/version2/sequences/FD004_train_X.npy")
sample = X[:1]

print("Shape :", sample.shape)

print()

print("Min :", sample.min())

print("Max :", sample.max())

print("Mean:", sample.mean())

print()

print(sample[0, :3])