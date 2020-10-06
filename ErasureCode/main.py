# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import encode
import decode

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    i = 0
    iteration_times = 100
    dataNum = 5  # should not be to large, 20 might be too big, usually 5~10
    dataMade = 3  # around dataNum/2
    dataLost = 3  # must less or equal to dataMade
    while i < iteration_times:
        encoder = encode.Encode(dataNum, dataMade)
        encoder.encoding()
        checker = decode.Check(dataLost)
        lostRows = checker.make_lost(encoder)
        decoder = decode.Decode(lostRows)
        decoder.decoding(encoder, checker)
        print(i)
        i = i + 1
