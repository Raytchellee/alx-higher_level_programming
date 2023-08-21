#!/usr/bin/python3
"""A class called Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class with attributes"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new class of instance Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """handles square size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """changes/updates the square values
            (id, size, x, y)
            **kwargs: New input key/value pairs
        """
        if args and len(args) is not 0:
            idx = 0
            for input_val in args:
                if idx == 0:
                    if input_val is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = input_val
                elif idx == 1:
                    self.size = input_val
                elif idx == 2:
                    self.x = input_val
                elif idx == 3:
                    self.y = input_val
                idx += 1

        elif kwargs and len(kwargs) is not 0:
            for keyy, val in kwargs.items():
                if keyy == "id":
                    if val is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = val
                elif keyy == "size":
                    self.size = val
                elif keyy == "x":
                    self.x = val
                elif keyy == "y":
                    self.y = val

    def to_dictionary(self):
        """displays square values in dictionary format"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """returns the properties description of the square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
