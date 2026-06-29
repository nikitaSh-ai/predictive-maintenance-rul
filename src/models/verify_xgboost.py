"""
verify_xgboost.py

Purpose:
Verify that all XGBoost outputs were generated successfully.
"""

import os

FILES = [
    "models/xgboost.pkl",
    "results/xgboost_metrics.txt",
    "results/xgboost_validation_predictions.csv",
    "results/xgboost_test_predictions.csv",
    "results/xgboost_prediction_vs_actual.png",
    "results/xgboost_residual_plot.png",
    "results/xgboost_feature_importance.csv",
    "results/xgboost_feature_importance.png"
]

print("=" * 60)
print("XGBOOST VERIFICATION")
print("=" * 60)

missing = False

for file in FILES:

    if os.path.exists(file):
        print(f"✓ {file}")
    else:
        print(f"✗ {file}")
        missing = True

print()

if not missing:
    print("=" * 60)
    print("XGBoost baseline completed successfully.")
else:
    print("=" * 60)
    print("Some files are missing.")