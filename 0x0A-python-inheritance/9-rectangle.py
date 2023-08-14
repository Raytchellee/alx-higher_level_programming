#!/usr/bin/python3
"""A rectangle class extend BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class extending BaseGeometry"""

    def __init__(self, width, height):
        """Creates a Rectangle Class
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)

    def area(self):
        """Gets area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Prints properties of the rectangle"""
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)
