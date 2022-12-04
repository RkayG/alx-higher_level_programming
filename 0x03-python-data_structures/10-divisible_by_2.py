#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """finds all multioles of 2 in a list"""
    if my_list:
        return [(i % 2 == 0) for i in my_list]
