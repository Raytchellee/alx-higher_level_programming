#!/usr/bin/python3
"""defines base geometry class"""


class BaseGeometry:
    """Defines base geometry"""
    def area(self):
        """gets area of geometry"""
        raise Exception('area() is not implemented')
    
    def integer_validator(self, name, value):
        """
        Checks for correct values
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
