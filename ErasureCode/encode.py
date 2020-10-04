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

    def read_data(self):
        # construct original data array and distribution matrix
        self.myData = np.random.randint(1000, size=(self.numOfData, 1), dtype=int)
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

class Decode():
    def __init__(self, lost):
        self.lost = lost.reshape(-1, 1)

    def decoding(self, encoder):
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
        self.originalData = self.originalData.astype(int)
        print("decoded original data:\n", self.originalData)
        if (np.array_equal(self.originalData, encoder.myData)):
            print("decode successfully!!")
        else:
            print("decode failed!!!")



    def abandon_lost(self, encoder):
        self.survivors = np.delete(encoder.encodeResults, self.lost, 0)
        self.myMatrixNow = np.delete(encoder.myMatrix, self.lost, 0)

if __name__ == "__main__":
    encoder = Encode(5,3)
    encoder.encoding()
    checker = Check(3)
    lostRows = checker.make_lost(encoder)
    decoder = Decode(lostRows)
    decoder.decoding(encoder)