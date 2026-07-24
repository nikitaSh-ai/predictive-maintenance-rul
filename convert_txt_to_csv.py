import pandas as pd

df = pd.read_csv(
    "DATA/raw/train_FD003.txt",
    sep=r"\s+",
    header=None
)

df.to_csv(
    "train_FD003.csv",
    index=False,
    header=False
)

print("CSV created successfully!")