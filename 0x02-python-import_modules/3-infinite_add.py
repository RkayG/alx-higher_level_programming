#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    len = len(argv)
    result = 0
    if len > 1:
        for i in range(1, len, 1):
            result += int(argv[i])
    print("{}".format(result))
