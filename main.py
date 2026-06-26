from src.data.data_loader import load_data

df = load_data("DATA/raw/train_FD001.txt")

print(df.head())

print("\nShape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())