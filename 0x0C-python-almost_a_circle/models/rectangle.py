#!/usr/bin/python3
"""A class called Rectangle"""
from models.base import Base


class Rectangle(Base):
    """A rectangle class with attributes"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new class of instance Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """handles rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """handles height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """handles rectangle's x coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """handles rectangle's y coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """gets(returns) area of rectangle"""
        return self.width * self.height

    def display(self):
        """prints rectangle of # characters"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for _ in range(self.y)]
        for _ in range(self.height):
            [print(" ", end="") for _ in range(self.x)]
            [print("#", end="") for _ in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """changes/updates the rectangle values
            (id, width, height, x, y)
            **kwargs: New input key/value pairs
        """
        if args and len(args) != 0:
            idx = 0
            for input_val in args:
                if idx == 0:
                    if input_val is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = input_val
                elif idx == 1:
                    self.width = input_val
                elif idx == 2:
                    self.height = input_val
                elif idx == 3:
                    self.x = input_val
                elif idx == 4:
                    self.y = input_val
                idx += 1

        elif kwargs and len(kwargs) != 0:
            for keyy, val in kwargs.items():
                if keyy == "id":
                    if val is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = val
                elif keyy == "width":
                    self.width = val
                elif keyy == "height":
                    self.height = val
                elif keyy == "x":
                    self.x = val
                elif keyy == "y":
                    self.y = val

    def to_dictionary(self):
        """displays rectangle values in dictionary format"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Returns the properties description of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
