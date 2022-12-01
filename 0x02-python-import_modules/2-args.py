#!/usr/bin/python3
from sys import argv
if __name == __main__:
    len = len(argv)
    if len == 2:
        print("1 argument:")
    elif len > 2:
        print("{} arguments:".format(len - 1))
    else:
        print("0 arguments.")
    for i in range(1, len, 1):
        print("{}: {}".format(i, argv[i]))
