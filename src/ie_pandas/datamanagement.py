# Data Manipulating Routines
import numpy as np


def _set_data_type(_arr):
    # Function to convert an array to the datatype (int, float, bool, string)
    _val = None
    try:
        _val = _arr.astype(np.int)

    except ValueError as att_err:
        try:
            _val = _arr.astype(np.float)
        except ValueError as att_err:
            if len(_arr[0]) in [4, 5]:
                _val = np.array([x == "True" for x in _arr])
            else:
                # string list has type as tuple so first element.
                _val = _set_string_array(_arr)
    finally:
        return _val


def _set_string_array(_arr):

    my_arr = np.array(_arr.tolist())

    return my_arr


def dict_as_arraytable(_dict):

    return np.array([list(item) for item in _dict.values()]).transpose()


def return_filtered_columns(data=None, cols=None):

    # This should be list column names.
    d1 = {}

    if cols is not None:
        if isinstance(cols, list):
            cols = np.array(cols)

        if isinstance(cols, np.ndarray):

            for col in cols:
                d1[col] = data.get(col)

        elif isinstance(cols, str):
            d1[cols] = data.get(cols)
        else:
            raise ValueError("should be Column or List of Column names.")

    return d1


def _array_to_dict(_data, _columns, _transpose=True):
    # function to turn array to dictionary.
    # if in row format, need to transpose.

    _df = None
    if _transpose is True:
        _df = _data.transpose()
    else:
        _df = _data

    d = {}

    for arg in range(len(_columns)):
        _arr = _df[arg]
        d[_columns[arg]] = _set_data_type(_arr)

    return d


def get_columnnames_by_numbers(df, _columns):
    _column_names = df.columns

    d = []
    for _col in _columns:
        d.append(_column_names[_col])

    return d
