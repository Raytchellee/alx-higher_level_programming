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
