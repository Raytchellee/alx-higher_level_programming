#!/usr/bin/python3
"""Documentation for python class"""


class Square:
    """A class example for square"""

    def __init__(self, size=0, position=(0, 0)):
        """initializes size as private"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        if (type(position) is not tuple or
                len(position) != 2 or
                not all(type(val) is int for val in position) or
                not all(val >= 0 for val in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """returns position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets position of self to value"""
        if (type(value) is not tuple or
                len(value) != 2 or
                not all(type(val) is int for val in value) or
                not all(val >= 0 for val in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __result__(self):
        '''square of hash'''
        res = []
        if self.__size == 0:
            return ''
        for _ in range((self.__position)[1]):
            res.append("\n")
        for _ in range(self.__size):
            for _ in range((self.__position)[0]):
                res.append(" ")
            for _ in range(self.__size):
                res.append("#")
            res.append('\n')
        return ''.join(res[:-1])

    def my_print(self):
        ''' prints self'''
        print(self)
