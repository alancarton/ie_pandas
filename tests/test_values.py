from ie_pandas import DataFrame
import numpy as np

_dataarray1 = np.array(
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
# _index=None
# _columns=None


def test_return_values_01():

    # The Initialization works, so testing that the values function is as expected.
    df = DataFrame(data=_dataarray1, index=_index, columns=_columns)

    expected = [
        ["1", "1.3254", "False", "R1"],
        ["3", "4.123", "True", "R 2"],
        ["3", "1.4", "False", "R 3"],
        ["2", "14.0", "False", "R 4"],
        ["12", "41.0", "True", "R5"],
    ]

    assert np.array_equal(df.values(), expected)
