from ie_pandas import DataFrame
import numpy as np
import pytest


def test_getrow():
    # Test whether get_row specifying the 4th row
    # returns the 4th row

    _data = np.array(
        [
            [1, 1.3254, False, "R1"],
            [3, 4.123, True, "R 2"],
            [3, 1.4, False, "R 3"],
            [2, 14.0, False, "R 4"],
            [12, 41.0, True, "R5"],
        ]
    )

    _columns = ["IntCol", "FloatCol", "BoolCol", "StringCol"]
    _index = [0, 1, 2, 3, 4]

    df = DataFrame(data=_data, index=_index, columns=_columns)
    row = 3
    expected_output = [2, 14.0, False, "R 4"]
    output = df.get_row(row)

    # Test if created object equals the desired object
    assert np.array_equal(output, expected_output)


def test_get_negative_row():
    # Tested behaviour: Return row counting from the end
    # when specifying a negative row key.

    _data = np.array(
        [
            [1, 1.3254, False, "R1"],
            [3, 4.123, True, "R 2"],
            [3, 1.4, False, "R 3"],
            [2, 14.0, False, "R 4"],
            [12, 41.0, True, "R5"],
        ]
    )

    _columns = ["IntCol", "FloatCol", "BoolCol", "StringCol"]
    _index = [0, 1, 2, 3, 4]

    df = DataFrame(data=_data, index=_index, columns=_columns)
    row = -1
    expected_output = [12, 41.0, True, "R5"]
    output = df.get_row(row)

    # Test if created object equals the desired object
    assert np.array_equal(output, expected_output)


def test_get_row_no_params():
    # Test whether get_row function returns a ValueError
    # when specifying no row

    # Use pytest structure for testing the error-handling
    with pytest.raises(ValueError) as ValError:
        _data = np.array(
            [
                [1, 1.3254, False, "R1"],
                [3, 4.123, True, "R 2"],
                [3, 1.4, False, "R 3"],
                [2, 14.0, False, "R 4"],
                [12, 41.0, True, "R5"],
            ]
        )

        _columns = ["IntCol", "FloatCol", "BoolCol", "StringCol"]
        _index = [0, 1, 2, 3, 4]

        df = DataFrame(data=_data, index=_index, columns=_columns)

        output = df.get_row()


def test_get_row_out_of_range():
    # Tests whether get_row function raises a ValueError
    # when specifying a row out of range

    # Use pytest structure for testing the error-handling
    with pytest.raises(ValueError) as ValError:

        _data = np.array(
            [
                [1, 1.3254, False, "R1"],
                [3, 4.123, True, "R 2"],
                [3, 1.4, False, "R 3"],
                [2, 14.0, False, "R 4"],
                [12, 41.0, True, "R5"],
            ]
        )

        _columns = ["IntCol", "FloatCol", "BoolCol", "StringCol"]
        _index = [0, 1, 2, 3, 4]

        df = DataFrame(data=_data, index=_index, columns=_columns)
        row = 5

        output = df.get_row(row)


def test_get_row_string_rowkey():
    # Tests whether get_row function raises a TypeError
    # when specifying a string as row key.

    # Use pytest structure for testing the error-handling
    with pytest.raises(TypeError) as TypError:

        _data = np.array(
            [
                [1, 1.3254, False, "R1"],
                [3, 4.123, True, "R 2"],
                [3, 1.4, False, "R 3"],
                [2, 14.0, False, "R 4"],
                [12, 41.0, True, "R5"],
            ]
        )

        _columns = ["IntCol", "FloatCol", "BoolCol", "StringCol"]
        _index = [0, 1, 2, 3, 4]

        df = DataFrame(data=_data, index=_index, columns=_columns)

        # Specify string as row index
        row = "a"

        output = df.get_row(row)
