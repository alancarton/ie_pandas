from ie_pandas import DataFrame
import numpy as np
import pytest


# Updating Test Scripts
def test_initialization_No_Params():
    with pytest.raises(ValueError) as ValError:
        df = DataFrame()
        # Error on Object Generation so Fail.  Data needed

        assert "InvalidConstructor" in str(ValError.value)


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
    _index = [0, 1, 2, 3, 4]

    try:
        df = DataFrame(data=_data, index=_index, columns=_columns)
        # Object Created so Pass Test.
        assert True

    except ValueError as Error:
        # Error on Object Generation so Fail
        assert False


def test_initialization_array_dict():
    _data = {
        "value1": [1, 2, 3, 4, 5, 6],
        "value2": [2, 2, 2, 2, 2, 2],
        "value3": [1.1, 2.2, 3.3, 4.4, 5.5, 6.6],
        "value4": ["a", "b", "c", "d", "e", "f"],
    }

    try:
        df = DataFrame(data=_data)

        assert True
    except ValueError as Error:

        assert False
