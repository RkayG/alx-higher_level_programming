#!/usr/bin/python3
def element_at(my_list, idx):
    """ retrieves elements from a list """
    if my_list:
        if idx < 0:
            return None
        elif idx >= len(my_list):
            return None
        return my_list[idx]
