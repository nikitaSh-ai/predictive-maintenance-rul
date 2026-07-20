import numpy as np

y = np.load("DATA/version2/sequences/FD001_train_y.npy")

print("Shape :", y.shape)
print("Min   :", y.min())
print("Max   :", y.max())
print("Mean  :", y.mean())
print("First 20 values:")
print(y[:20])