import pandas as pd
import pytest

from src.pipeline.predict_engine_v2 import (
    validate_dataset,
    EXPECTED_COLUMN_NAMES,
)




def create_valid_dataframe():
    """
    Create a valid NASA C-MAPSS style dataframe.
    """

    data = {}

    for column in EXPECTED_COLUMN_NAMES:

        if column == "engine_id":

            data[column] = [1, 1, 1]

        elif column == "cycle":

            data[column] = [1, 2, 3]

        else:

            data[column] = [0.5, 0.6, 0.7]

    return pd.DataFrame(data)





def test_valid_dataset():

    """
    A completely valid dataset
    should pass validation.
    """

    df = create_valid_dataframe()

    assert validate_dataset(df) is True




def test_empty_dataset():

    df = pd.DataFrame()

    with pytest.raises(ValueError):

        validate_dataset(df)








def test_duplicate_rows():

    columns = [
        "engine_id",
        "cycle",
        "op_setting_1",
        "op_setting_2",
        "op_setting_3",
        *[f"sensor_{i}" for i in range(1, 22)]
    ]

    row = [1, 1] + [0] * 24

    df = pd.DataFrame(
        [row, row],
        columns=columns
    )

    with pytest.raises(ValueError):

        validate_dataset(df)









def test_missing_values():

    df = create_valid_dataframe()

    df.loc[0, "sensor_2"] = None

    with pytest.raises(ValueError):

        validate_dataset(df)




def test_non_numeric_values():

    df = create_valid_dataframe()

    df["sensor_2"] = df["sensor_2"].astype(object)

    df.loc[0, "sensor_2"] = "abc"

    with pytest.raises(ValueError):

        validate_dataset(df)



def test_invalid_engine_id():

    df = create_valid_dataframe()

    df.loc[0, "engine_id"] = -1

    with pytest.raises(ValueError):

        validate_dataset(df)





def test_invalid_column_count():

    df = create_valid_dataframe()

    df = df.drop(columns=["sensor_21"])

    with pytest.raises(ValueError):

        validate_dataset(df)




def test_negative_cycle():

    df = create_valid_dataframe()

    df.loc[0, "cycle"] = -5

    with pytest.raises(ValueError):

        validate_dataset(df)




def test_unsorted_cycles():

    df = create_valid_dataframe()

    df["cycle"] = [1, 3, 2]

    with pytest.raises(ValueError):

        validate_dataset(df)