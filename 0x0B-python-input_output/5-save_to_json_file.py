#!/usr/bin/python3
"""
Module: 5-save_to_json_file.py
Object-to-textfile in JSON
"""
import json

def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation
    Args:
        my_obj: object to be written to file
        filename: file to be written to
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
