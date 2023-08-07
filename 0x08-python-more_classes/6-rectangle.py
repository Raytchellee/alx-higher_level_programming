#!/usr/bin/python3
"""A Rectangle Class in Python"""


class Rectangle:
    """A typical rectangle Class definition in Python

    Attributes:
        number_of_instances: Total available instances
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize new Rectangle

        Args:
            width: Rectangle width
            height: Rectangle height
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """controls width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """controls height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Gets rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Gets perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Prints a rectangle of # characters
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        hashes = []
        for idx in range(self.__height):
            for _ in range(self.__width):
                hashes.append("#")
            if idx != self.__height - 1:
                hashes.append("\n")
        return ("".join(hashes))

    def __repr__(self):
        """Creates a new rectangle class"""
        res = "Rectangle("
        res += str(self.__width) + ", "
        res += str(self.__height) + ")"
        return (res)

    def __del__(self):
        """Prints message for any deleted rectangle"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
