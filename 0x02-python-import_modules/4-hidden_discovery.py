#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for i in dir(hidden_4):
        if not i.startwith("__"):
            print("{}".format(i))
