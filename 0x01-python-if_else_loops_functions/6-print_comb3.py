#!/usr/bin/python3
for a in range(0, 10):
    for b in range(1, 10):
        if a == b or a > b:
            continue
        if a == 8 and b == 9:
            print("{}{}".format(a, b))
        print("{}{}".format(a, b), end=", ")
