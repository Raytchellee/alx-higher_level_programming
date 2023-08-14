#!/usr/bin/python3
"""Prints sorted list in ascending order"""


class MyList(list):
    """Prints sorted list in ascending order"""

    def print_sorted(self):
        """Prints sorted list in ascending order"""
        print(sorted(self))
