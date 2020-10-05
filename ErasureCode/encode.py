# This python file is used for encoding input data

import numpy as np
import sys


class Encode():
    def __init__(self, n, m):
        """
        :param n: the number of divided parts from original data
        :param m: the number of which will be encoded parts from original data
        """
        self.numOfData = n
        self.numOfCoded = m
        self.numOfDataColumns = 5000

    def read_data(self):
        # construct original data array and distribution matrix
        maxValue = 1000
        self.myData = np.random.uniform(0, maxValue, size=(self.numOfData, self.numOfDataColumns))
        upPartMatrix = np.identity(self.numOfData, dtype=int)
        lowMatrix = np.vander(np.array([1, 2, 3, 4, 5]), self.numOfCoded, increasing=True)
        self.myMatrix = np.concatenate((upPartMatrix, lowMatrix.transpose()), axis=0)
        print("Original data:\n", self.myData)
        print("read finished!!")

    def encoding(self):
        # construct the encoded parts from original data
        self.read_data()
        self.encodeResults = np.dot(self.myMatrix, self.myData)
        print("encoding finished!!")

class Check():
    def __init__(self, n):
        self.numOfLost = n

    def make_lost(self, encoder):
        """
        :param encoder: the instance of class Encode
        :return: array of rows which to delete
        """
        encoded_shape = encoder.encodeResults.shape
        lost = np.random.choice(encoded_shape[0], self.numOfLost, replace=False)
        print(lost)
        return lost

    def array_precision_equal(self, a1, a2):
        """
        :param a1: input array 1
        :param a2: input array 2
        :return: bool, Returns True if the arrays are equal.
        """
        try:
            a1, a2 = np.asarray(a1), np.asarray(a2)
        except Exception:
            return False
        if a1.shape != a2.shape:
            return False
        decimalNum = 4     # rarely, there are some precision mismatch between some elements in arrays
        a1 = np.around(a1, decimals=decimalNum)
        a2 = np.around(a2, decimals=decimalNum)
        for idx, x in np.ndenumerate(a1):
            temp_a1 = x
            temp_a2 = a2[idx]
            if temp_a1 != temp_a2:
                print("not equal element:", temp_a1, " vs ", temp_a2)
                return False

        return True


class Decode():
    def __init__(self, lost):
        self.lost = lost.reshape(-1, 1)

    def decoding(self, encoder, checker):
        """
        :param encoder: the instance of class Encode
        :return:
        """
        self.abandon_lost(encoder)
        try:
            tempInverse = np.linalg.inv(self.myMatrixNow)
        except np.linalg.LinAlgError:
            # Not invertible. Skip this one.
            pass
        self.originalData = np.dot(tempInverse, self.survivors)
        print("decoded original data:\n", self.originalData)
        if (checker.array_precision_equal(self.originalData, encoder.myData)):
            print("decode successfully!!")
        else:
            print("decode failed!!!")
            sys.exit()

    def abandon_lost(self, encoder):
        self.survivors = np.delete(encoder.encodeResults, self.lost, 0)
        self.myMatrixNow = np.delete(encoder.myMatrix, self.lost, 0)

if __name__ == "__main__":
    i = 0
    iteration_times = 100
    while i < iteration_times:
        encoder = Encode(5, 3)
        encoder.encoding()
        checker = Check(3)
        lostRows = checker.make_lost(encoder)
        decoder = Decode(lostRows)
        decoder.decoding(encoder, checker)
        print(i)
        i = i+1