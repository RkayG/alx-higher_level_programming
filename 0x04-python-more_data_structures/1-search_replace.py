#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list is not None:
        for elem in range(len(my_list)):
            if my_list[elem] == search:
                my_list[elem] = replace
        return my_list
    return None
