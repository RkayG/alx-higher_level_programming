#!/usr/bin/python3
"""
Module: 1-write_file.py
Writes to a file
"""


def write_file(filename="", text=""):
    """
    Writes string to UTF8 text file
    Args:
        filename: file to be written to
        text: string to write
    Return: number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
