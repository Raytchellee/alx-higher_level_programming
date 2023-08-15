#!/usr/bin/python3
"""writes object to file using json format"""
import json


def save_to_json_file(my_obj, filename):
    """a function that writes object to file using json format"""
    with open(filename, mode="w", encoding="utf-8") as input_file:
        json.dump(my_obj, input_file)
