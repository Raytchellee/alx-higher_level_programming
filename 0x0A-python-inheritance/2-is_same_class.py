#!/usr/bin/python3
"""checks if a class is same"""


def is_same_class(obj, a_class):
    """checks if input obj is instace of class"""

    if type(obj) == a_class:
        return True
    return False
