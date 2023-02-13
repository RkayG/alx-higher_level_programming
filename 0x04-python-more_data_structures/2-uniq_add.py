#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Add all unique integers in a list (once for each integer)."""
    if my_list is not None:
        result = 0
        for x in set(my_list):
            result += x
        return result
    return None
