# coding: utf-8

# In[ ]:


import numpy as np


def unique_element(self):
    return np.array(
        [
            np.unique(self.df[col], return_counts=True)
            if col in self.numericals
            else None
            for col in self.column_names
        ]
    )
