#!/usr/bin/python3
"""A function that looks up the list of available attributes and methods"""


def lookup(obj):
    """returns the list of available attributes and methods"""
    return (dir(obj))
