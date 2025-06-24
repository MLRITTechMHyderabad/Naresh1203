"""You are given a string S and width W. Your task is to wrap the string into a paragraph of width.
If the following string is given as input to the program:
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Then, the output of the program should be:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ"""

import textwrap

def wrap_string(s, w):
    return textwrap.fill(s, w)

if __name__ == "__main__":
    s = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
    w = 4
    print(wrap_string(s, w))
