

# coding: utf-8

# In[ ]:


import numpy as np


def mean(self):
    return np.array(
        [
            np.mean(self.df[col]) if col in self.numericals else None
            for col in self.column_names
        ]
    )


def percentile(self):
    for x in [25,50,75]:
        return np.array(
            [
                np.percentile(self.df[col], x) if col in self.numericals else None
                for col in self.column_names
            ]
        )
