#!/usr/bin/python3
"""reads an input file"""


def read_file(filename=""):
    """A function that reads an input file"""

    with open(filename, encoding='utf-8') as input_file:
        print(input_file.read(), end="")
