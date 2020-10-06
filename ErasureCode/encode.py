# This python file is used for encoding input data

import numpy as np



class Encode():
    def __init__(self, n, m):
        """
        :param n: the number of divided parts from original data
        :param m: the number of which will be encoded parts from original data
        """
        self.numOfData = n
        self.numOfCoded = m
        self.numOfDataColumns = 50000

    def read_data(self):
        # construct original data array and distribution matrix
        maxValue = 1000
        self.myData = np.random.uniform(0, maxValue, size=(self.numOfData, self.numOfDataColumns))
        upPartMatrix = np.identity(self.numOfData, dtype=np.int64)
        # 自然数矩阵
        lowMatrix = np.vander(np.arange(1, self.numOfData+1, dtype=np.int64), self.numOfCoded, increasing=True)
        self.myMatrix = np.concatenate((upPartMatrix, lowMatrix.transpose()), axis=0)
        print("Original data:\n", self.myData)
        print("read finished!!")

    def encoding(self):
        # construct the encoded parts from original data
        self.read_data()
        self.encodeResults = np.dot(self.myMatrix, self.myData)
        print("encoding finished!!")
