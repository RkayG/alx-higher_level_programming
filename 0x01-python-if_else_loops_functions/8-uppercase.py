#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if str[i] >= chr(97) and str[i] <= chr(122):
            str = chr(ord(str[i]) - 32)
    return str[i]
