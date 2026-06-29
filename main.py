#from src.data.data_loader import load_data
#df = load_data("DATA/raw/train_FD001.txt")
#print(df.head())
#print("\nShape:", df.shape)

#print("\nColumns:")
#print(df.columns.tolist())







"""
main.py

Project:
Explainable Predictive Maintenance Decision Support System
for Remaining Useful Life Prediction

Author: Nikita Sharma

Purpose:
Entry point of the project.
"""

#print("=" * 60)
#print("Explainable Predictive Maintenance")
#print("=" * 60)

#print("\nProject initialized successfully.")
















"""
main.py

Project:
Explainable Predictive Maintenance Decision Support System
for Remaining Useful Life Prediction

Purpose:
Entry point of the project.
"""

"""PIPELINE_STEPS = [
    "Data Validation",
    "Engine Split",
    "Split Verification",
    "RUL Generation",
    "Dataset Creation",
    "Feature Analysis",
    "Constant Feature Detection",
    "Feature Selection",
    "Feature Scaling",
    "Sequence Generation",
    "Random Forest Baseline",
    "XGBoost Baseline",
    "GRU Training",
    "Model Evaluation",
    "SHAP Explainability",
    "Uncertainty Estimation",
    "Risk Assessment",
    "Maintenance Recommendation Engine",
    "Decision Support System"
]

print("=" * 60)
print("Explainable Predictive Maintenance")
print("=" * 60)

print("\nProject Pipeline:\n")

for i, step in enumerate(PIPELINE_STEPS, start=1):
    print(f"{i:02d}. {step}")

print("\nPipeline initialized successfully.")     """


























 
# restart : 
"""
main.py

Explainable Predictive Maintenance using NASA CMAPSS FD001

This file orchestrates the complete preprocessing pipeline.
"""

from src.data.data_validation import validate_data
from src.data.data_loader import load_data
from src.data.engine_split import create_engine_split
from src.data.verify_engine_split import verify_engine_split
from src.data.build_datasets import build_datasets

from src.features.feature_analysis import analyze_features
from src.features.check_constant_features import check_constant_features
from src.features.feature_selection import select_features
from src.features.scale_features import scale_features


def preprocessing_pipeline():
    """
    Run the complete preprocessing pipeline.
    """

    print("\n" + "=" * 60)
    print("PREPROCESSING PIPELINE")
    print("=" * 60)

    # Load raw dataset
    df = load_data("DATA/raw/train_FD001.txt")

    print("\n[1/8] Data Validation")
    validate_data(df)

    print("\n[2/8] Engine Split")
    create_engine_split(df)

    print("\n[3/8] Split Verification")
    verify_engine_split()

    print("\n[4/8] Dataset Creation")
    build_datasets()

    print("\n[5/8] Feature Analysis")
    analyze_features()

    print("\n[6/8] Constant Feature Detection")
    check_constant_features()

    print("\n[7/8] Feature Selection")
    select_features()

    print("\n[8/8] Feature Scaling")
    scale_features()

    print("\n" + "=" * 60)
    print("PREPROCESSING COMPLETED SUCCESSFULLY")
    print("=" * 60)


def main():

    print("=" * 60)
    print("Explainable Predictive Maintenance")
    print("=" * 60)

    preprocessing_pipeline()


if __name__ == "__main__":
    main()