#!/usr/bin/python3
"""inserts a text after certain string"""


def append_after(filename="", search_string="", new_string=""):
    """adds text after lines containing search_string in file"""
    result = ""
    with open(filename) as input_file:
        for row in input_file:
            result += row
            if search_string in row:
                result += new_string
    with open(filename, "w") as output_file:
        output_file.write(result)
