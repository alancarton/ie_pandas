from ie_pandas import DataFrame
import numpy as np


def test_std_df():
    # Test if standard usage of std works as expected
    # Including only acting on numerical columns

    data = {
        "value1": [1, 2, 3, 4, 5, 6],
        "value2": [-2, 4, 6, 2, 10, 0],
        "value3": [1.1, 2.2, 3.3, 4.4, 5.5, 6.6],
        "value4": ["a", "b", "c", "d", "e", "f"],
    }

    expected_output = np.array(
        [
            np.array([1, 2, 3, 4, 5, 6]).std(),
            np.array([-2, 4, 6, 2, 10, 0]).std(),
            np.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6]).std(),
            None,
        ]
    )

    df = DataFrame(data)
    std_output = df.std()

    assert std_output.all() == expected_output.all()
