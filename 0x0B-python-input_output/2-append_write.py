#!/usr/bin/python3
"""
Module: 2-append_write.py
Appends to a file
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file (UTF8)
    Args:
        filename: file to be opened
        text: string to append
    Return: number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
