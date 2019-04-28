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
