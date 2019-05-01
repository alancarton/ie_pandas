from ie_pandas import DataFrame
import numpy as np
import pytest


# Updating Test Scripts
def test_initialization_No_Params():
    with pytest.raises(ValueError) as ValError:
        # Error on Object Generation so Fail.  Data needed
        df = DataFrame()


def test_initialization_array_param():

    _data = np.array(
        [
            [1, 1.3254, False, "R1"],
            [3, 4.123, True, "R 2"],
            [3, 1.4, False, "R 3"],
            [2, 14, False, "R 4"],
            [12, 41, True, "R5"],
        ]
    )

    _columns = ["IntCol", "FloatCol", "BoolCol", "StringCol"]

    df = DataFrame(data=_data, columns=_columns)
    # Object Created so Pass Test.
    assert True


def test_initialization_dict():

    _data = {
        "value1": [1, 2, 3, 4, 5, 6],
        "value2": [True, False, False, True, True, True],
        "value3": [1.1, 2.2, 3.3, 4.4, 5.5, 6.6],
        "value4": ["a", "b", "c", "d", "e", "f"],
    }

    df = DataFrame(data=_data)

    assert True


def test_initialization_array_no_columns():

    _data = np.array(
        [
            [1, 1.3254, False, "R1"],
            [3, 4.123, True, "R 2"],
            [3, 1.4, False, "R 3"],
            [2, 14, False, "R 4"],
            [12, 41, True, "R5"],
        ]
    )

    df = DataFrame(data=_data)
    # Object Created so Pass Test.
    assert True
