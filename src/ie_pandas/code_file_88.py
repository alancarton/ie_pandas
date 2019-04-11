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
            _NUMERIC_KINDS = set('buifc')
            # check if the array is numerical or not
            # because for non-numerical values, can't do mathematical operation
            if data_dict[key].dtype.kind in _NUMERIC_KINDS:
                numeric_cols.append(key)
            else:
                not_numeric_cols.append(key)
        self.column_names = [*data_dict.keys()]
        self.df = data_dict
        self.numericals = numeric_cols
        self.non_numericals = not_numeric_cols
        
    # need to check if each feature's values are in the numpy array format
    # if not, then convert them to numpy array
    # but before convert, need to check the datatype of each feature, if it's string,
    # then can't convert directly
    def sum(self):
        return np.array([self.df[col].sum() if col in self.numericals else None for col in self.column_names])
    def median(self):
        return np.array([np.median(self.df[col]) if col in self.numericals else None for col in self.column_names])
    def min(self):
        return np.array([self.df[col].min() if col in self.numericals else None for col in self.column_names])
    def max(self):
        return np.array([self.df[col].max() if col in self.numericals else None for col in self.column_names])