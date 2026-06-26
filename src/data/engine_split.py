import json
import os

from src.data.data_loader import load_data


def create_engine_split(df):
    """
    Create engine-level train/validation/test split.
    """

    engines = sorted(df["engine_id"].unique())

    train_engines = [int(e) for e in engines[:70]]
    val_engines = [int(e) for e in engines[70:85]]
    test_engines = [int(e) for e in engines[85:]]

    split = {
        "train": train_engines,
        "validation": val_engines,
        "test": test_engines
    }

    os.makedirs("DATA/processed", exist_ok=True)

    with open("DATA/processed/engine_split.json", "w") as f:
        json.dump(split, f, indent=4)

    print("Engine split saved successfully.")
    print(f"Train Engines      : {len(train_engines)}")
    print(f"Validation Engines : {len(val_engines)}")
    print(f"Test Engines       : {len(test_engines)}")


if __name__ == "__main__":
    df = load_data("DATA/raw/train_FD001.txt")
    create_engine_split(df)