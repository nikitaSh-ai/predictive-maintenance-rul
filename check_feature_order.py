import pandas as pd

df = pd.read_csv("DATA/version2/scaled/FD001_train.csv")

feature_columns = [
    c for c in df.columns
    if c not in [
        "engine_id",
        "cycle",
        "max_cycle",
        "RUL",
        "RUL_CLIPPED",
    ]
]

print(feature_columns)