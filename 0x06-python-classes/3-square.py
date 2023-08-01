#!/usr/bin/python3
"""Documentation for python class"""


class Square:
    """A class example for square"""

    def __init__(self, size=0):
        """initializes size as private"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
