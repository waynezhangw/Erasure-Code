# This python file is used for encoding input data

import numpy as np

from numpy import random

class Encode():
    def __init__(self, n, m):
        self.numOfData = n
        self.numOfCoded = m

    def read_data(self):
        print("read finished!!")



if __name__ == "__main__":
    encoder = Encode(5,3)
    encoder.read_data()
    b = np.array([1,2])
    print(b)