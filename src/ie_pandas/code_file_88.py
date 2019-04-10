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