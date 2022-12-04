#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """ replaces an element of a list at a specific
        position
    """
    if my_list:
        if idx < 0 or idx >= len(my_list):
            return my_list
        if idx is not None and element is not None:
            my_list[idx] = element
        return my_list
