# Code File 04

import numpy as np
from ie_pandas import DataFrame


def test_std_df():
    data = {
        "value1": [1, 2, 3, 4, 5, 6],
        "value2": [2, 4, 6, 2, 10, 0],
        "value3": [1.1, 2.2, 3.3, 4.4, 5.5, 6.6],
        "value4": ["a", "b", "c", "d", "e", "f"],
    }
    expected_output = np.array(
        [
            np.array([1, 2, 3, 4, 5, 6]).std(),
            np.array([2, 4, 6, 2, 10, 0]).std(),
            np.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6]).std(),
            None,
        ]
    )

    df = DataFrame(data)
    mean_output = df.mean()
    print(mean_output)
    print(expected_output)

    assert mean_output.all() == expected_output.all()


def std(self):
    return np.array(
        [
            self.df[col].std() if col in self.numericals else None
            for col in self.column_names
        ]
    )


def get_row(self, rowindex=None):
    data = self.data

    if not isinstance(rowindex, int):
        raise TypeError("Row index must be an integer.")

    if rowindex is None:
        raise ValueError("Must specify row index.")

    if abs(rowindex) > len(data):
        raise ValueError("Row index out of range")

    d_temp = {}

    for key in data.keys():
        d_temp[key] = data.get(key)[rowindex]

    return list(d_temp.values())


from ie_pandas import DataFrame
import numpy as np


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


def test_get_row_No_Params():
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

        # Specify string as row index
        row = "a"

        output = df.get_row(row)
