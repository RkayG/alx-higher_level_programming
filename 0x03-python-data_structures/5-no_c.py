#!/usr/bin/python3
def no_c(my_string):
    """ removes all characters c and C from a string."""
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        print("{}".format(i), end="")
    print("")
