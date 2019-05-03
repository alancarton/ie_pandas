from .datamanagement import _array_to_dict, return_filtered_columns
from .datamanagement import dict_as_arraytable, _set_string_array
from .datamanagement import _set_data_type
import matplotlib.pyplot as plt
import numpy as np

print("Added ...")


class DataFrame:
    def __init__(self, data=None, dtype="Row", columns=None):
        """
        ie_pandas DataFrame
        Some functionality implemented to mimic Pandas DataFrame.
        Will throw error on Creation if created as DataFrame()
        Args:
            data [Required: Dictionary or Array of Data]
            data as Dictionary :
                    Columns as keys.
                    Data Values as array of data of same type
                data as Array :
                    array format can be by row or column in array.
                    dtype [Optional for Array Data: ("Row" / "Col")
                        Default is "Row"
                    columns [Optional: (Array of columns.
                        If missing uses [0, 1, 2 ... etc]) ]
        """
        data_dict = {}

        if not (data is None):
            if not isinstance(data, dict):
                # data is not Dictionary is Array, so reshape to Dictionary.

                t_transpose = True

                if dtype == "Row":
                    _shape = data.shape

                    if columns is None:
                        # columns are keys for Dictionary
                        columns = np.array(range(_shape[1]))

                else:
                    # Array in column format
                    _shape = data.shape

                    if columns is None:
                        # columns are keys for Dictionary
                        columns = np.array(range(_shape[0]))

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

        else:
            raise ValueError("Invalid Constructor. Use Dictionary or Array!")

    def values(self, colnames=None):
        """
        values: Returns values as dictionary.
        args:
            colnames: List of column names [Optional].
                If omitted returns all columns for data in the order specified.
        """
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

    def get_row(self, rowindex=None):
        """
        get_row: Returns row as a list of values.
        args:
                 rowindex: Zero-based index of row to be returned.
        In case a negative index is provided, will count
        backwards from the last row.
        """
        data = self.data

        if rowindex is None:
            raise ValueError("Must specify row index.")

        if not isinstance(rowindex, int):
            raise TypeError("Row index must be an integer.")

        if abs(rowindex) > len(data):
            raise ValueError("Row index out of range")

        # Create empty dictionary and add in elements of desired row.

        d_temp = {}
        for key in data.keys():
            d_temp[key] = data.get(key)[rowindex]

        # Return result as list
        return list(d_temp.values())

    @property
    def data(self):
        """
        data: Property: Returns DataFrame data as Dictionary.
              No parameters required.
        args: None
        """
        _df = self.df
        return _df

    @data.setter
    def data(self, value):
        """
        data: Property: Sets DataFrame data as Dictionary.
              No parameters required.
        args: None
        """
        _df = DataFrame(value)
        self.df = _df.data

    def to_array(self, colnames=None):
        """
        to_array: Returns Data Values for DataFrame array.
        args:     colnames: Array of Column names [Optional]
                    will default to all columns if missing.
                    Will return the data as an array in the order specified.
        """
        _df = self.values(colnames)
        return dict_as_arraytable(_df)

    def __repr__(self):

        return str(self.data)

    def __str__(self):
        return "ie-pandas DataFrame"

    # Basic metrics
    def sum(self):
        """
        sum:    Returns array with the sum of each numeric column.
                No parameters required.
        args:   None
        """
        # return the sum for the numerical features
        # for non-numerical return none
        return np.array(
            [
                self.df[col].sum() if col in self.numericals else None
                for col in self.column_names
            ]
        )

    def median(self):
        """
        median: Returns array with the median of each numeric column.
                No parameters required.
        args:   None
        """
        # return the median for the numerical features
        # for non-numerical return none
        return np.array(
            [
                np.median(self.df[col]) if col in self.numericals else None
                for col in self.column_names
            ]
        )

    def min(self):
        """
        min:    Returns array with the minimum value of each numeric column.
                No parameters required.
        args:   None
        """
        # return the min for the numerical features
        # for non-numerical return none
        return np.array(
            [
                self.df[col].min() if col in self.numericals else None
                for col in self.column_names
            ]
        )

    def max(self):
        """
        max:    Returns array with the maximum value of each numeric column.
                No parameters required.
        args:   None
        """
        # return the max for the numerical features
        # for non-numerical return none
        return np.array(
            [
                self.df[col].max() if col in self.numericals else None
                for col in self.column_names
            ]
        )

    def mean(self):
        """
        mean:   Returns array with the mean of each numeric column.
                No parameters required.
        args:   None
        """
        # return the mean for the numerical features
        # for non-numerical return none
        return np.array(
            [
                np.mean(self.df[col]) if col in self.numericals else None
                for col in self.column_names
            ]
        )

    def percentile(self):
        """
        percentile: Returns array with the 0.25, 0.5 and 0.75
                    percentiles of each numeric column.
                    No parameters required.
        args:       None
        """
        _df = self.df
        _nums = self.numericals
        for x in [25, 50, 75]:
            return np.array(
                [
                    np.percentile(_df[col], x) if col in _nums else None
                    for col in self.column_names
                ]
            )

    def std(self):
        """
        std:    Returns array with standard deviation of numeric columns.
                No parameters required.
        args:   None
        """
        return np.array(
            [
                self.df[col].std() if col in self.numericals else None
                for col in self.column_names
            ]
        )

    def unique_element(self):
        return np.array([np.unique(self.df[col]) for col in self.column_names])

    @property
    def columns(self):
        """
            columns: Returns the list of columns for the DataFrame.
            args:    None.
        """
        lst_cols = -1
        try:
            lst_cols = list(self.column_names)
            return lst_cols
        except Exception as ex:
            log_traceback(ex)

    @columns.setter
    def columns(self, value):
        """
            columns:	Sets the list of columns for the DataFrame
            args:		value: Column List as array.
        """
        # Rebuilds the data dictionary using the new value as keys.
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

    def _hist(self, cols=[], bins=None, color=None, rwidth=0.9):
        """
        bins : int or sequence or str, optional
        histtype : {'bar', 'barstacked', 'step', 'stepfilled'}, optional
        color : color or array_like of colors or None, optional
        rwidth : scalar or None, optional
        """
        # check if cols is list, raise error if not
        if not isinstance(cols, (list,)):
            raise ValueError("The argument cols must be empty or a list")
        # define histogram function
        # takes numerical features

        def draw_hist(nums):
            fig1, ax1 = plt.subplots()
            ax1.set_title(nums)
            ax1.hist(self.df[nums], bins=bins, color=color, rwidth=rwidth)

        # if cols is not passed, plot all numericals
        if not cols:
            for nums in self.numericals:
                draw_hist(nums)
        # if cols is passed as a list
        # then plot only the numericals
        else:
            for nums in cols:
                if nums in self.numericals:
                    draw_hist(nums)
                else:
                    print(f"column: {nums} must be numerical.")

    def unique_element(self):
        return np.array([np.unique(self.df[col]) for col in self.column_names])

    def _boxplot(self, cols=[], vert=True, meanline=False):
        """
        vert : bool, optional (True)
        meanline : bool, optional (False)
        """
        if not isinstance(cols, (list,)):
            raise ValueError("The argument cols must be empty or a list")
        # define boxplot function
        # takes numerical features

        def draw_box(nums):
            fig1, ax1 = plt.subplots()
            ax1.set_title(nums)
            ax1.boxplot(self.df[nums], vert=vert, meanline=meanline)

        # if _boxplot not pass list of columns
        # then take all the numerical features
        if not cols:
            for nums in self.numericals:
                draw_box(nums)
        # if specifies columns then check if numerical
        # and then plot the numericals
        else:
            for nums in cols:
                if nums in self.numericals:
                    draw_box(nums)
                else:
                    print(f"column: {nums} must be numerical.")
