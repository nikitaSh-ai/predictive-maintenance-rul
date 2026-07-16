"""
validate_deployment.py

Purpose:
Validate the deployed prediction
pipeline using unseen engine files.
"""


import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]

sys.path.append(str(ROOT_DIR))
from pathlib import Path
import pandas as pd
import numpy as np

from src.pipeline.predict_engine import run_prediction


if len(sys.argv) != 2:

    print("Usage:")
    print("python scripts/validate_deployment.py FD001")
    sys.exit(1)

DATASET = sys.argv[1].upper()



VALIDATION_FOLDER = (
    ROOT_DIR
    / "DATA"
    / "validation"
    / DATASET
)

GROUND_TRUTH_FILE = (
    ROOT_DIR
    / "DATA"
    / "raw"
    / f"RUL_{DATASET}.txt"
)


print("=" * 70)
print(f"DEPLOYMENT VALIDATION : {DATASET}")
print("=" * 70)

if not VALIDATION_FOLDER.exists():
    raise FileNotFoundError(
        f"Validation folder not found:\n{VALIDATION_FOLDER}"
    )

if not GROUND_TRUTH_FILE.exists():
    raise FileNotFoundError(
        f"Ground truth file not found:\n{GROUND_TRUTH_FILE}"
    )

def validate_deployment():

    ground_truth = pd.read_csv(
        GROUND_TRUTH_FILE,
        header=None,
        names=["actual_rul"]
    )

    results = []

    validation_files = sorted(
        VALIDATION_FOLDER.glob("engine_*.csv")
    )

    for file in validation_files:

        print(f"\nProcessing {file.name}...")

        engine_id = int(
            file.stem.split("_")[1]
        )

        prediction = run_prediction(str(file))

        predicted_rul = prediction["predicted_rul"]

        actual_rul = ground_truth.iloc[
            engine_id - 1
        ]["actual_rul"]

        error = abs(
            predicted_rul - actual_rul
        )

        results.append(
            {
                "Engine": engine_id,
                "Actual RUL": actual_rul,
                "Predicted RUL": predicted_rul,
                "Absolute Error": round(error, 2),
            }
        )

    results_df = pd.DataFrame(results)

    mae = results_df["Absolute Error"].mean()

    rmse = np.sqrt(
        (
            (
                results_df["Predicted RUL"]
                -
                results_df["Actual RUL"]
            ) ** 2
        ).mean()
    )

    best_prediction = results_df.loc[
        results_df["Absolute Error"].idxmin()
    ]

    worst_prediction = results_df.loc[
        results_df["Absolute Error"].idxmax()
    ]

    print("\n")
    print("=" * 70)
    print("DEPLOYMENT VALIDATION RESULTS")
    print("=" * 70)

    print(results_df)

    print("\n")
    print(f"MAE  : {mae:.2f} cycles")
    print(f"RMSE : {rmse:.2f} cycles")

    print("\nBest Prediction")
    print(best_prediction)

    print("\nWorst Prediction")
    print(worst_prediction)

    output_file = (
    VALIDATION_FOLDER
    / "deployment_validation_results.csv"
    )

    results_df.to_csv(
        output_file,
        index=False,
    )

    print(
        f"\nResults saved to:\n{output_file}"
    )


if __name__ == "__main__":
    validate_deployment()