#!/usr/bin/python3
"""
Module: 3-say_my_name.py
"""


def say_my_name(first_name, last_name=""):
    """
    Function: prints a string containing first
    name and last name
    Args: first_name, last_name (last_name can be empty)
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
