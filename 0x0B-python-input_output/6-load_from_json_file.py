#!/usr/bin/python3
"""
Module: 6-load_from_json_file.py
creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    Function: creates a Python Object from a JSON file
    Args:
        filename: JSON file
    """
    with open(filename) as f:
        return json.load(f)
