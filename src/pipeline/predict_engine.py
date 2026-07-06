"""
predict_engine.py

Purpose:
Execute the complete prediction pipeline
for a new engine dataset.
"""



import pandas as pd
import os


def validate_dataset(df):
    """
    Validate uploaded dataset.
    """

    print("\nValidating Dataset...")

    if df.empty:

        raise ValueError(
            "Uploaded dataset is empty."
        )

    print("Dataset is not empty.")

    expected_columns = 26

    if df.shape[1] != expected_columns:

      raise ValueError(
        f"Expected {expected_columns} columns but found {df.shape[1]}."
     )

    print("Column count is valid.")


    try:

      df = df.apply(pd.to_numeric)

      print("All values are numeric.")

    except Exception:

      raise ValueError(
        "Dataset contains non-numeric values."
      )
    



    # -------------------------
    # Check Missing Values
    # -------------------------

    missing_values = df.isnull().sum().sum()

    if missing_values > 0:

      raise ValueError(
        f"Dataset contains {missing_values} missing values."
    )

    print("No missing values found.")

    return True







def split_by_engine(df):
    """
    Split the uploaded dataset
    into individual engines.
    """

    print("\nSplitting Dataset by Engine...")

    engines = {}

    engine_ids = df.iloc[:, 0].unique()

    for engine_id in engine_ids:

        engine_df = df[
            df.iloc[:, 0] == engine_id
        ].copy()

        engines[engine_id] = engine_df

    print(f"Number of Engines : {len(engines)}")

    return engines









def extract_latest_sequence(
    engine_df,
    sequence_length=40
):
    """
    Extract the latest sequence
    from one engine.
    """

    print(
        f"\nEngine {engine_df.iloc[0,0]}"
    )

    print(
        f"Cycles : {len(engine_df)}"
    )

    if len(engine_df) < sequence_length:

        return None

    latest_sequence = engine_df.tail(
        sequence_length
    )

    print(
        "Latest Sequence Shape :",
        latest_sequence.shape
    )

    return latest_sequence







def run_prediction(csv_path):
    """
    Run the complete prediction pipeline.

    Parameters
    ----------
    csv_path : str
        Path of uploaded CSV file.

    Returns
    -------
    dict
        Prediction results.
    """

    print("=" * 60)
    print("PREDICTION PIPELINE")
    print("=" * 60)

    print("\nInput File")
    print(csv_path)

    # -------------------------
    # Load Uploaded CSV
    # -------------------------

 

    extension = os.path.splitext(csv_path)[1].lower()

    if extension == ".csv":

      df = pd.read_csv(csv_path)

    elif extension == ".txt":

     df = pd.read_csv(
        csv_path,
        sep=r"\s+",
        header=None
      )

    else:

      raise ValueError(
        "Unsupported file format."
       )

    print("\nDataset Loaded Successfully.")
 
    print(df.head())

    print("\nDataset Shape")

    print(df.shape)

    validate_dataset(df)

    engines = split_by_engine(df)

    print("\nEngine IDs")

    print(list(engines.keys())[:10])


    first_engine = engines[1]

    sequence = extract_latest_sequence(
    first_engine
     )

    return df



if __name__ == "__main__":

    run_prediction(
        "DATA/raw/train_FD001.txt"
    )