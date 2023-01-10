#!/usr/bin/python3
"""
Module: 3-to_json_string.py
represents a string in JSON
"""
import json


def to_json_string(my_obj):
    """
    Returns a JSON representation of a string
    Args:
        my_obj: string to represent
    """
    return json.dumps(my_obj)
