"""
create_validation_files.py

Purpose:
Create validation engine CSV files
from any NASA C-MAPSS test dataset.

Usage:
python scripts/create_validation_files.py FD001
python scripts/create_validation_files.py FD002
python scripts/create_validation_files.py FD003
python scripts/create_validation_files.py FD004
"""

from pathlib import Path
import pandas as pd
import sys

ROOT_DIR = Path(__file__).resolve().parents[1]

if len(sys.argv) != 2:
    print("Usage:")
    print("python scripts/create_validation_files.py FD001")
    sys.exit(1)

dataset = sys.argv[1].upper()

TEST_FILE = ROOT_DIR / "DATA" / "raw" / f"test_{dataset}.txt"

OUTPUT_FOLDER = ROOT_DIR / "DATA" / "validation" / dataset
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

if not TEST_FILE.exists():
    raise FileNotFoundError(TEST_FILE)

df = pd.read_csv(
    TEST_FILE,
    sep=r"\s+",
    header=None
)

df.columns = [
    "engine_id",
    "cycle",
    "op_setting_1",
    "op_setting_2",
    "op_setting_3",
    "sensor_1",
    "sensor_2",
    "sensor_3",
    "sensor_4",
    "sensor_5",
    "sensor_6",
    "sensor_7",
    "sensor_8",
    "sensor_9",
    "sensor_10",
    "sensor_11",
    "sensor_12",
    "sensor_13",
    "sensor_14",
    "sensor_15",
    "sensor_16",
    "sensor_17",
    "sensor_18",
    "sensor_19",
    "sensor_20",
    "sensor_21",
]

engine_ids = sorted(df["engine_id"].unique())

print(f"\nDataset : {dataset}")
print(f"Total Engines : {len(engine_ids)}")

# Select five representative engines
indices = [
    0,
    len(engine_ids) // 4,
    len(engine_ids) // 2,
    (3 * len(engine_ids)) // 4,
    len(engine_ids) - 1,
]

selected_engines = sorted(
    list(
        {
            engine_ids[i]
            for i in indices
        }
    )
)

print("\nSelected Engines:")
print(selected_engines)

for engine in selected_engines:

    engine_df = df[
        df["engine_id"] == engine
    ]

    output_file = OUTPUT_FOLDER / f"engine_{engine}.csv"

    engine_df.to_csv(
        output_file,
        index=False
    )

    print(
        f"✓ Engine {engine} exported ({len(engine_df)} rows)"
    )

print("\nValidation dataset created successfully.")
print(f"Saved to: {OUTPUT_FOLDER}")