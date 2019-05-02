# coding: utf-8

# In[ ]:


from ie_pandas import DataFrame
import numpy as np


def test_mean_df():
    data = {
        "value1": [1, 2, 3, 4, 5, 6],
        "value2": [2, 4, 6, 2, 10, 0],
        "value3": [1.1, 2.2, 3.3, 4.4, 5.5, 6.6],
        "value4": ["a", "b", "c", "d", "e", "f"],
    }
    expected_output = np.array([3.5, 4, 3.85, None])
    df = DataFrame(data)
    mean_output = df.mean()
    print(mean_output)
    print(expected_output)

    assert mean_output.all() == expected_output.all()


def test_percentile_df():
    data = {
        "value1": [1, 2, 3, 4, 5],
        "value2": [2, 4, 6, 8, 10],
        "value3": ["a", "b", "c", "d", "e"],
    }
    expected_output = np.array([[2, 3, 4], [4, 6, 8], [None, None, None]])
    df = DataFrame(data)
    percentile_output = df.percentile()
    print(percentile_output)
    print(expected_output)

    assert percentile_output.all() == expected_output.all()


def test_unique_df():

    data = {
        "value1": [1, 2, 3, 4, 5, 6],
        "value2": [2, 4, 6, 2, 2, 0],
        "value3": [1, 1, 1, 1, 1, 1],
    }

    expected_output = np.array(
        [np.array([1, 2, 3, 4, 5, 6]), np.array([0, 2, 4, 6]), np.array([1])]
    )
    df = DataFrame(data)
    unique_element_output = df.unique_element()

    for i in range(len(unique_element_output)):
        assert unique_element_output[i].all() == expected_output[i].all()
