#!/usr/bin/python3
"""A rectangle class extend BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class extending BaseGeometry"""

    def __init__(self, width, height):
        """Creates a Rectangle Class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
