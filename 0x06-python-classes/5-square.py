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

    @property
    def size(self):
        """returns size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets size of self to value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """prints a square of #"""
        if (self.__size) == 0:
            print()
        for idx in range(self.__size):
            [print("#", end="") for idy in range(self.__size)]
            print()
