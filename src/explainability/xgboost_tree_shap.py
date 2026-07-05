"""
xgboost_tree_shap.py

Purpose:
Generate feature explanations
using XGBoost's native
Tree SHAP implementation.
"""

import joblib
import xgboost as xgb
import numpy as np

def main():

    print("=" * 60)
    print("XGBOOST NATIVE TREE SHAP")
    print("=" * 60)


    # ---------------------------------
    # Load XGBoost Model
    # ---------------------------------

    model = joblib.load(
    "models/xgboost.pkl"
    )

    print("\nXGBoost model loaded successfully.")




    # ---------------------------------
    # Load Test Data
    # ---------------------------------

    X_test = np.load(
    "DATA/sequences/X_test.npy"
    )

    y_test = np.load(
    "DATA/sequences/y_test.npy"
     )

    print("\nOriginal Shape")
    print("X_test :", X_test.shape)

    X_test = X_test.reshape(
    X_test.shape[0],
    -1
    )

    print("\nFlattened Shape")
    print("X_test :", X_test.shape)
    print("y_test :", y_test.shape)




    # ---------------------------------
    # Get Booster
    # ---------------------------------

    booster = model.get_booster()

    print("\nBooster loaded successfully.")



    # ---------------------------------
    # Create DMatrix
    # ---------------------------------

    explain_data = X_test[:100]

    dtest = xgb.DMatrix(explain_data)

    print("\nDMatrix created successfully.")
    print("Explain Shape :", explain_data.shape)



    # ---------------------------------
    # Native Tree SHAP
    # ---------------------------------
    print("STEP 1")

    shap_values = booster.predict(
    dtest,
    pred_contribs=True
    )

    print("STEP 2")

    print("\nNative Tree SHAP computed successfully.")

    print("SHAP Shape :")
    print(shap_values.shape)






if __name__ == "__main__":
    main()