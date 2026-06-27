# If even one engine appears in both training and testing: Random Forest becomes optimistic, XGBoost becomes optimistic. GRU becomes optimistic. SHAP explanations become misleading. The evaluation is no longer trustworthy.


"""
verify_engine_split.py

Purpose:
Verify that the engine-level Train/Validation/Test split
contains no overlapping engine IDs.
"""

import json


def verify_engine_split():
    """
    Verify engine split integrity.
    """

    with open("DATA/processed/engine_split.json", "r") as f:
        split = json.load(f)

    train = set(split["train"])
    validation = set(split["validation"])
    test = set(split["test"])

    print("=" * 50)
    print("ENGINE SPLIT VERIFICATION")
    print("=" * 50)

    print("\nTrain Engines:", len(train))
    print("Validation Engines:", len(validation))
    print("Test Engines:", len(test))

    print("\nOverlap Checks")

    print(
        "Train ∩ Validation:",
        len(train.intersection(validation))
    )

    print(
        "Train ∩ Test:",
        len(train.intersection(test))
    )

    print(
        "Validation ∩ Test:",
        len(validation.intersection(test))
    )

    all_engines = train.union(validation).union(test)

    print("\nTotal Unique Engines:", len(all_engines))


def main():
    """
    Run engine split verification.
    """
    verify_engine_split()


if __name__ == "__main__":
    main()