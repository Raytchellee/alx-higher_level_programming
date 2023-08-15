#!/usr/bin/python3
""" returns the dictionary description of an object"""


def class_to_json(obj):
    """function that serializes a class"""
    return obj.__dict__
