#!/usr/bin/python3
"""appends into an input filename"""


def append_write(filename="", text=""):
    """appends input text to a file"""
    with open(filename, mode="a", encoding='utf-8') as input_file:
        return (input_file.write(text))
