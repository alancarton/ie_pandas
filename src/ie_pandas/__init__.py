from .code_file_01 import get_array
from .code_file_88 import sum_df,median_df,min_df,max_df

print("Added ...")
import datetime as dt
import sys
import numpy as np

# class DataFrame():
#     def __init__(self, array):
#         self._nparray = array
    
#     def array_2(self):
#         return get_array(self._nparray)

# assume the object is already in dictionary
class DataFrame():

    def __init__(self,data_dict):
        # list variables for numerical and non numerical keys
        numeric_cols = []
        not_numeric_cols = []
        # loop over every key of the dictionary, and convert to numpy array
        for key,value in data_dict.items():
            if not isinstance(data_dict[key],(np.ndarray)):
                data_dict[key]=np.asarray(data_dict[key])
            # check if the array is numerical or not
            # because for non-numerical values, can't do mathematical operation
            _NUMERIC_KINDS = set('buifc')
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
