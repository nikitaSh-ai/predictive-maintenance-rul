"""
verify_random_forest.py

Purpose:
Verify that all Random Forest outputs were generated successfully.
"""

from pathlib import Path

files = [
    "models/random_forest.pkl",
    "results/random_forest_metrics.txt",
    "results/random_forest_validation_predictions.csv",
    "results/random_forest_test_predictions.csv",
    "results/random_forest_prediction_vs_actual.png",
    "results/random_forest_residual_plot.png",
    "results/random_forest_feature_importance.csv",
    "results/random_forest_feature_importance.png"
]

print("=" * 60)
print("RANDOM FOREST VERIFICATION")
print("=" * 60)

all_ok = True

for file in files:
    if Path(file).exists():
        print(f"✓ {file}")
    else:
        print(f"✗ {file}")
        all_ok = False

print("\n" + "=" * 60)

if all_ok:
    print("Random Forest baseline completed successfully.")
else:
    print("Some output files are missing.")