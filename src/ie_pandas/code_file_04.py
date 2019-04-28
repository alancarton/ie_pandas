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


# Create the test first
# def test_head():
# 	dataframe =


# def head(self, l=6):
# 	return np.array(
# 		[
# 			self.df[1:l] if l>=
# 		]
# 	)
