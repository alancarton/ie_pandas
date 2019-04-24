import numpy as np


def sum_df(self):
    return np.array(
        [
            self.df[col].sum() if col in self.numericals else None
            for col in self.column_names
        ]
    )


def median_df(self):
    return np.array(
        [
            np.median(self.df[col]) if col in self.numericals else None
            for col in self.column_names
        ]
    )


def min_df(self):
    return np.array(
        [
            self.df[col].min() if col in self.numericals else None
            for col in self.column_names
        ]
    )


def max_df(self):
    return np.array(
        [
            self.df[col].max() if col in self.numericals else None
            for col in self.column_names
        ]
    )
