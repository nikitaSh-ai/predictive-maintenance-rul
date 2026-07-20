import numpy as np
import torch

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

X = np.load("DATA/version2/sequences/FD004_test_X.npy")
y = np.load("DATA/version2/sequences/FD004_test_y.npy")

sample = torch.FloatTensor(X[:10])

with torch.no_grad():
    pred = model(sample).squeeze().numpy()

print("Prediction:")
print(pred)

print()

print("Ground Truth:")
print(y[:10])













