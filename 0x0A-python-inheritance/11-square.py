#!/usr/bin/python3
"""Creates a square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Creates square class"""

    def __init__(self, size):
        """Defines a square class"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ returns the area of the square"""
        return super().area()

    def __str__(self):
        """returns class contents of the square"""
        side = str(self.__size)
        return "[Square] " + side + "/" + side
