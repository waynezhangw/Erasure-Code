# This python file is used for decoding data,
# recover original data from left data (some lost)

import numpy as np
import sys


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
            sys.exit(["matrix not invertible"])
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


class Check():
    def __init__(self, n):
        self.numOfLost = n

    def make_lost(self, encoder):
        """
        :param encoder: the instance of class Encode
        :return: array of rows which to delete
        """
        if self.numOfLost > encoder.numOfCoded:
            sys.exit(["lost too much"])
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