print("code file from scott")
print("just double check")

# assume the object is already in dictionary
class DataFrame():
    def __init__(self,data_dict):
        self.column_names = [*data_dict.keys()]
        self.df = data_dict
    # add .sum()
    def sum(self):
        return np.array([self.df[col].sum() for col in self.column_names])
    def median(self):
        return np.array([np.median(self.df[col]) for col in self.column_names])
    def min(self):
        return np.array([self.df[col].min() for col in self.column_names])
    def max(self):
        return np.array([self.df[col].max() for col in self.column_names])