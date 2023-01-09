#!/usr/bin/python3
"""
Module: 0-lookup
"""


def lookup(obj):
    """
    Returns list of available attributes and methods
    of an object.
    """
    my_list = [attr for attr in dir(obj)]
    return my_list
