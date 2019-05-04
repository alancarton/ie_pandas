from ie_pandas import DataFrame
import numpy as np

_dataarray1 = np.array(
    [
        [1, 1.3254, False, "R1"],
        [3, 4.123, True, "R 2"],
        [3, 1.4, False, "R 3"],
        [2, 14.0, False, "R 4"],
        [12, 41.0, True, "R5"],
    ]
)

_columns = ["IntCol", "FloatCol", "BoolCol", "StringCol"]


def test_return_values_01():

    # itialization works, testing that the values function is as expected.
    df = DataFrame(data=_dataarray1, columns=_columns)

    expected = [
        ["1", "1.3254", "False", "R1"],
        ["3", "4.123", "True", "R 2"],
        ["3", "1.4", "False", "R 3"],
        ["2", "14.0", "False", "R 4"],
        ["12", "41.0", "True", "R5"],
    ]

    assert np.array_equal(df.to_array(), expected)


def test_return_values_02():

    # itialization works, testing that the values function is as expected.
    df = DataFrame(data=_dataarray1, columns=_columns)

    expected = [
        ["1", "1.3254", "False", "R1"],
        ["3", "4.123", "True", "R 2"],
        ["3", "1.4", "False", "R 3"],
        ["2", "14.0", "False", "R 4"],
        ["12", "41.0", "True", "R5"],
    ]

    assert np.array_equal(df.to_array([0, 1, 2, 3]), expected)


def test_return_values_03():

    # itialization works, testing that the values function is as expected.
    df = DataFrame(data=_dataarray1, columns=_columns)
    # Can reorganize and specify columns by position
    expected = [
        ["1.3254", "1", "R1", "False"],
        ["4.123", "3", "R 2", "True"],
        ["1.4", "3", "R 3", "False"],
        ["14.0", "2", "R 4", "False"],
        ["41.0", "12", "R5", "True"],
    ]

    assert np.array_equal(df.to_array([1, 0, 3, 2]), expected)


def test_return_values_04():

    # itialization works, testing that the values function is as expected.
    df = DataFrame(data=_dataarray1, columns=_columns)
    # Can reorganize and specify columns by column name
    expected = [
        ["1.3254", "1", "R1", "False"],
        ["4.123", "3", "R 2", "True"],
        ["1.4", "3", "R 3", "False"],
        ["14.0", "2", "R 4", "False"],
        ["41.0", "12", "R5", "True"],
    ]

    assert np.array_equal(
        df.to_array(["FloatCol", "IntCol", "StringCol", "BoolCol"]), expected
    )
