import numpy as np


def sum(self):
    return np.array([self.df[col].sum() if col in self.numericals else None for col in self.column_names])
def median(self):
    return np.array([np.median(self.df[col]) if col in self.numericals else None for col in self.column_names])
def min(self):
    return np.array([self.df[col].min() if col in self.numericals else None for col in self.column_names])
def max(self):
    return np.array([self.df[col].max() if col in self.numericals else None for col in self.column_names])