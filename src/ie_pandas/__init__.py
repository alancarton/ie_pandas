from .code_file_01 import get_array

print("Added ...")
import datetime as dt
import sys
import numpy as np

class DataFrame():
    def __init__(self, array):
        self._nparray = array
    
    def array_2(self):
        return get_array(self._nparray)

