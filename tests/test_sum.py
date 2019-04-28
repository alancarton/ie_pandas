from ie_pandas import DataFrame
import numpy as np


def test_sum_df():
    data = {
        "value1": [1, 2, 3, 4, 5, 6],
        "value2": [2, 2, 2, 2, 2, 2],
        "value3": [1.1, 2.2, 3.3, 4.4, 5.5, 6.6],
        "value4": ["a", "b", "c", "d", "e", "f"],
    }
    expected_output = np.array([21, 12, 23.1, None])
    df = DataFrame(data)
    sum_output = df.sum()
    print(sum_output)
    print(expected_output)

    assert sum_output.all() == expected_output.all()


def test_median_df():
    data = {
        "value1": [1, 2, 3, 4, 5, 6],
        "value2": [2, 2, 2, 2, 2, 2],
        "value3": [1.1, 2.2, 3.3, 4.4, 5.5, 6.6],
        "value4": ["a", "b", "c", "d", "e", "f"],
    }
    expected_output = np.array([3.5, 2, 3.85, None])
    df = DataFrame(data)
    median_output = df.median()
    print(median_output)
    print(expected_output)

    assert median_output.all() == expected_output.all()


def test_min_df():
    data = {
        "value1": [1, 2, 3, 4, 5, 6],
        "value2": [2, 2, 2, 2, 2, 2],
        "value3": [1.1, 2.2, 3.3, 4.4, 5.5, 6.6],
        "value4": ["a", "b", "c", "d", "e", "f"],
    }
    expected_output = np.array([1, 2, 1.1, None])
    df = DataFrame(data)
    min_output = df.min()
    print(min_output)
    print(expected_output)

    assert min_output.all() == expected_output.all()


def test_max_df():
    data = {
        "value1": [1, 2, 3, 4, 5, 6],
        "value2": [2, 2, 2, 2, 2, 2],
        "value3": [1.1, 2.2, 3.3, 4.4, 5.5, 6.6],
        "value4": ["a", "b", "c", "d", "e", "f"],
    }
    expected_output = np.array([6, 2, 6.6, None])
    df = DataFrame(data)
    max_output = df.max()
    print(max_output)
    print(expected_output)

    assert max_output.all() == expected_output.all()
