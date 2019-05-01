from ie_pandas import DataFrame
import numpy as np
import pytest

_data = np.array(
    [
        [1, 1.3254, False, "R1"],
        [3, 4.123, True, "R 2"],
        [3, 1.4, False, "R 3"],
        [2, 14.0, False, "R 4"],
        [12, 41.0, True, "R5"],
    ]
)


def test_check_value():

    _columns = ["IntCol", "FloatCol", "BoolCol", "StringCol"]
    dframe = DataFrame(data=_data, columns=_columns)
    df = dframe.df
    # set the value
    expectedval = 4.123

    assert df["FloatCol"][1] == expectedval


def test_check_set_value():

    _columns = ["IntCol", "FloatCol", "BoolCol", "StringCol"]
    dframe = DataFrame(data=_data, columns=_columns)
    df = dframe.df

    # set the value
    expectedval = 2
    df["IntCol"][1] = 2

    assert df["IntCol"][1] == expectedval


def test_check_set_None():

    _columns = ["IntCol", "FloatCol", "BoolCol", "StringCol"]
    dframe = DataFrame(data=_data, columns=_columns)
    df = dframe.df

    # set the value
    originalval = df["FloatCol"][1]
    df["FloatCol"][1] = np.NaN

    assert not (df["FloatCol"][1] == originalval)


def test_check_set_columns():

    _columns = ["1", "2", "3", "4"]
    dframe = DataFrame(data=_data, columns=_columns)
    _new_columns = ["IntCol", "FloatCol", "BoolCol", "StringCol"]

    # Get the current value of second column "2"
    originalval = dframe.df["2"][1]
    # set the Column Names to something more descriptive
    dframe.columns = _new_columns
    df = dframe.df

    assert df["FloatCol"][1] == originalval


def test_set_value_():

    _columns = ["IntCol", "FloatCol", "BoolCol", "StringCol"]
    df = DataFrame(data=_data, columns=_columns)
    # This should fail, as cannot assign String to Int Column
    # Bool will convert to 1 for numeric. Float will round to integer.
    with pytest.raises(ValueError) as ValError:
        df.df["IntCol"][1] = "This Is a Test"
