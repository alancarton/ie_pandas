from .code_file_01 import get_array
from .code_file_88 import sum_df, median_df, min_df, max_df, _hist, _boxplot
from .code_file_89 import mean as mean_df
from .code_file_89 import percentile as percentile_df
from .datamanagement import _array_to_dict, return_filtered_columns
from .datamanagement import dict_as_arraytable, _set_string_array
from .datamanagement import _set_data_type
import matplotlib.pyplot as plt
import numpy as np

print("Added ...")


class DataFrame:
    def __init__(self, data=None, dtype="Row", index=None, columns=None):

        data_dict = {}

        if not (data is None):
            if not isinstance(data, dict):
                # data is not Dictionary is Array, so reshape to Dictionary.

                t_transpose = True

                if dtype == "Row":
                    _shape = data.shape

                    if columns is None:
                        # columns are keys for Dictionary
                        columns = np.array(range(_shape[0] + 1))
                    if index is None:
                        index = np.array(range(_shape[1] + 1))

                else:
                    # Array in column format
                    _shape = data.shape

                    if columns is None:
                        # columns are keys for Dictionary
                        columns = np.array(range(_shape[1] + 1))
                    if index is None:
                        index = np.array(range(_shape[0] + 1))

                    t_transpose = False

                data_dict = _array_to_dict(data, columns, t_transpose)

            else:
                # Is Dictionary.
                data_dict = data
        else:
            raise ValueError("Invalid Constructor. Use Dictionary or Array!")

        # Now that data is in common format, store it properly
        if not (data_dict is None):
            numeric_cols = []
            not_numeric_cols = []
            # loop over every key of the dictionary, and convert to numpy array
            for key, value in data_dict.items():
                if not isinstance(data_dict[key], (np.ndarray)):
                    data_dict[key] = np.asarray(data_dict[key])
                # check if the array is numerical or not because for
                # non-numerical values, can't do mathematical operation
                _NUMERIC_KINDS = set("buifc")
                if data_dict[key].dtype.kind in _NUMERIC_KINDS:
                    numeric_cols.append(key)
                else:
                    not_numeric_cols.append(key)

            self.df = data_dict
            self.column_names = [*data_dict.keys()]
            self.numericals = numeric_cols
            self.non_numericals = not_numeric_cols

            if index is None:
                _key = self.column_names[0]
                my_index = np.array(range(len(self.df.get(_key))))
            else:
                my_index = index

            self.index = my_index
        else:
            raise ValueError("Invalid Constructor. Use Dictionary or Array!")

    def values(self, colnames=None):
        _df = None
        _cols = self.columns
        if colnames is None:
            # Return all columns
            _df = self.df
        else:
            # Colnames needs to be an array.
            if not isinstance(colnames, np.ndarray):
                colnames = np.array(colnames)

            if not type(colnames[0]) is str:
                # Numeric list, so get list as column names.
                _cols = get_columnnames_by_numbers(colnames)
            else:
                _cols = colnames

            _df = return_filtered_columns(self.df, cols=_cols)

        return _df

    @property
    def data(self):
        _df = self.df
        return _df

    @data.setter
    def data(self, value):
        self.df = value

    def to_array(self, colnames=None):
        _df = self.values(colnames)

        return dict_as_arraytable(_df)

    def __repr__(self):

        return str(self.data())

    def __str__(self):
        return "ie-pandas DataFrame"

    def sum(self):
        return sum_df(self)

    def median(self):
        return median_df(self)

    def min(self):
        return min_df(self)

    def max(self):
        return max_df(self)

    def mean(self):
        return mean_df(self)

    def percentile(self):
        return percentile_df(self)

    @property
    def columns(self):

        lst_cols = -1
        try:
            lst_cols = list(self.column_names)
            return lst_cols
        except Exception as ex:
            log_traceback(ex)

    @columns.setter
    def columns(self, value):

        d = self.data
        d1 = {}
        new_key = 0
        for key in d.keys():
            d1[value[new_key]] = d.get(key)
            new_key += 1

        self.data = d1
        self.column_names = value

    @property
    def index(self):

        lst_rows = -1
        try:
            lst_rows = self.index_names
            return lst_rows
        except Exception as ex:
            log_traceback(ex)

    @index.setter
    def index(self, value):
        self.index_names = value

    def get_col_numbers(self, _columns):
        _arr = []

        _columncheck = self.column_names

        for _colcheck in _columncheck:
            int_col = 0
            for _col in _columns:
                if _colcheck == _col:
                    _arr.append(int_col)
                int_col += 1

        return _arr

    def icol(self, cols=None):
        # Unsure if this works ...
        _keys = list(self.df.keys())
        _df = self.df
        if cols is not None:
            d1 = {}
            if isinstance(cols, list):
                for col in cols:
                    d1[_keys[col]] = _df.get(_keys[col])
            elif isinstance(cols, int):
                d1[_keys[cols]] = _df.get(_keys[cols])
            else:
                raise ValueError(
                    "Column Number or List",
                    "Column needs to be Integer or Integer list.",
                )
        return np.array(d1.items())

    def row(self, rowname):
        return self.columns.index(rowname)

    def ___col_by_names(self, cols):

        _arr = self.get_col_numbers(self.column_names, cols)
        return self.icol(_arr)

    def loc(self, rowname, colname):
        rtn_ = None
        if (rowname is None) and (colname is None):
            rtn_ = self.iloc[:, :]
        elif col is None:
            _row = self.row(self, rowname)
            rtn_ = self.iloc[_row, :]
        elif row is None:
            _col = self.col(self, colname)
            rtn_ = self.iloc[:, _col]
        else:
            _row = self.row(rowname)
            _col = self.col(colname)
            rtn_ = self.iloc[_row, _col]
        return rtn_

    def hist(self):
        return _hist(self)

    def boxplot(self):
        return _boxplot(self)
