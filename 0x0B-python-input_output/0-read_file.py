#!/usr/bin/python3
"""
Module: 0-read_file.py
Reads a file
"""


def read_file(filename=""):
    """
    Prints the content of a file encoded in UTF8 to stdout
    Args:
        filename: file to be opened
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
