from ie_pandas import DataFrame
import numpy as np


def test_check_value():

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
    dframe = DataFrame(data=_data, index=_index, columns=_columns)
    df = dframe.df
    # set the value
    expectedval = 4.123

    assert df["FloatCol"][1] == expectedval


def test_check_set_value():

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
    dframe = DataFrame(data=_data, index=_index, columns=_columns)
    df = dframe.df

    # set the value
    expectedval = 2
    df["IntCol"][1] = 2

    assert df["IntCol"][1] == expectedval


def test_check_set_None():

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
    dframe = DataFrame(data=_data, index=_index, columns=_columns)
    df = dframe.df

    # set the value
    originalval = df["FloatCol"][1]
    df["FloatCol"][1] = np.NaN

    assert not (df["FloatCol"][1] == originalval)
