#!/usr/bin/python3
"""checks if a class is same"""


def is_kind_of_class(obj, a_class):
    """
    Checks if obj is same class as a_class
    """

    if isinstance(obj, a_class):
        return True
    return False
