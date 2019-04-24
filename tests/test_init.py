from ie_pandas import DataFrame
import numpy as np

# Updating Test Scripts
def test_initialization_No_Params():

    try:
        df = DataFrame()

        assert False
    except ValueError as Error:

        assert True


def test_initialization_array_param():

    _data = np.array(
        [
            ["", "IntCol", "FloatCol", "BoolCol", "StringCol"],
            [1, 1, 1.3254, False, "Test Row 1"],
            [2, 3, 4.123, True, "Test Row 2"],
            [3, 3, 1.4, False, "Test Row 3"],
            [4, 2, 14, False, "Test Row 4"],
        ]
    )

    _columns = _data[0, 1:]
    _index = _data[1:, 0]

    try:
        df = DataFrame(data=_data, index=_index, columns=_columns)

        assert True
    except ValueError as Error:

        assert False


def test_initialization_array_dict():
    _data = {
        "value1": [1, 2, 3, 4, 5, 6],
        "value2": [2, 2, 2, 2, 2, 2],
        "value3": [1.1, 2.2, 3.3, 4.4, 5.5, 6.6],
        "value4": ["a", "b", "c", "d", "e", "f"],
    }

    try:
        df = DataFrame(data_dict=_data)

        assert True
    except ValueError as Error:

        assert False