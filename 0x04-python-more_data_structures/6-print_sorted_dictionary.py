#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        for key, val in sorted(a_dictionary.items()):
            print("{}: {}".format(key, val))
    return
