#!/usr/bin/python3
"""defines base geometry class"""


class BaseGeometry:
    """Defines base geometry"""
    def area(self):
        """gets area of geometry"""
        raise Exception('area() is not implemented')
