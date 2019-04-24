from .code_file_88 import sum_df, median_df, min_df, max_df

print("Added ...")
import datetime as dt
import sys
import numpy as np

from .code_file_88 import sum_df, median_df, min_df, max_df

print("Added ...")
import datetime as dt
import sys
import numpy as np


class DataFrame:
    def __init__(self, data_dict=None, data=None, index=None, columns=None):

        if not (all([data_dict is None, data is None])) and any(
            [data_dict is None, data is None]
        ):
            # All OK
            pass
        else:
            raise ValueError(
                "InvalidConstructor",
                "DataFrame constructor not properly called. Use Dictionary or Array!",
            )

        if not (data is None):
            data_dict = dict(enumerate(data))
            # Need to get this into dictionary and pass to below instead of this.

        if not (data_dict is None):
            numeric_cols = []
            not_numeric_cols = []
            # loop over every key of the dictionary, and convert to numpy array
            for key, value in data_dict.items():
                if not isinstance(data_dict[key], (np.ndarray)):
                    data_dict[key] = np.asarray(data_dict[key])
                    # check if the array is numerical or not
            # because for non-numerical values, can't do mathematical operation
            _NUMERIC_KINDS = set("buifc")
            if data_dict[key].dtype.kind in _NUMERIC_KINDS:
                numeric_cols.append(key)
            else:
                not_numeric_cols.append(key)

            self.column_names = [*data_dict.keys()]
            self.df = data_dict
            self.numericals = numeric_cols
            self.non_numericals = not_numeric_cols

    def sum(self):
        return sum_df(self)

    def median(self):
        return median_df(self)

    def min(self):
        return min_df(self)

    def max(self):
        return max_df(self)