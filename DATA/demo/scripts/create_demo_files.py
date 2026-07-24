import pandas as pd
from pathlib import Path

# NASA column names
columns = (
    ["engine_id", "cycle"]
    + [f"op_setting_{i}" for i in range(1, 4)]
    + [f"sensor_{i}" for i in range(1, 22)]
)

# Change this path if your project structure is different
input_file = "DATA/raw/train_FD001.txt"

df = pd.read_csv(
    input_file,
    sep=r"\s+",
    header=None,
    names=columns
)

# Select Engine 1
engine = df[df["engine_id"] == 1].copy()

# Output folder
output_dir = Path("DATA/demo")
output_dir.mkdir(parents=True, exist_ok=True)

# Create demo datasets
engine.iloc[:60].to_csv(output_dir / "Engine1_60.csv", index=False)
engine.iloc[:120].to_csv(output_dir / "Engine1_120.csv", index=False)
engine.to_csv(output_dir / "Engine1_192.csv", index=False)

print("Demo files created successfully!")