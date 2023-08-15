#!/usr/bin/python3
"""writes into an input filename"""


def write_file(filename="", text=""):
    """writes input text to a file"""
    with open(filename, mode="w", encoding='utf-8') as input_file:
        return (input_file.write(text))
