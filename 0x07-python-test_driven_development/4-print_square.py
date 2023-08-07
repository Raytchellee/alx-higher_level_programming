#!/usr/bin/python3
"""Function that prints a square of #"""


def print_square(size):
    """Prints a squre of #

    Args:
        size: Square size
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print("")
