#!/usr/bin/python3
"""Function for name printing"""


def say_my_name(first_name, last_name=""):
    """Prints out name

    Args:
        first_name: Input first name
        last_name: Input last name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
