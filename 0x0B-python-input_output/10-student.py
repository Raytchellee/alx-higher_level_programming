#!/usr/bin/python3
"""A student class in Python"""


class Student:
    """Defines attributes of  a student"""
    def __init__(self, first_name, last_name, age):
        """initializes student attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """serializes student attributes"""
        if attrs is None:
            return self.__dict__
        else:
            temp = {}
            for key in attrs:
                if type(key) != str:
                    return self.__dict__
            for key in attrs:
                if key in self.__dict__:
                    temp[key] = self.__dict__[key]
            return temp
