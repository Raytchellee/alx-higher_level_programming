#!/usr/bin/python3
"""converts file to json object"""
import json


def load_from_json_file(filename):
    """a function that converts file to json object"""
    with open(filename) as input_file:
        return json.load(input_file)
