#!/usr/bin/python3

import math


class MagicClass:
    """magic calculation class in python"""
    def __init__(self, radius=0):
        """initialize self radius"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """calculate area of a circle"""
        return  math.pi * (self.__radius ** 2)

    def circumference(self):
        """find the circumference of a circle"""
        return 2 * self.__radius * math.pi
