#!/usr/bin/python3
"""Creates a model class called Base"""
import turtle
import json
import csv


class Base:
    """The base model class with attributes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a class of instance Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts object to a serialized json"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        this_file = cls.__name__ + ".json"

        with open(this_file, "w") as new_file:
            if list_objs is None:
                new_file.write("[]")
            else:
                items = [item.to_dictionary() for item in list_objs]
                new_file.write(Base.to_json_string(items))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """that returns an instance with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Square":
                this_class = cls(1)
            else:
                this_class = cls(1, 1)
            this_class.update(**dictionary)
            return this_class

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        this_file = str(cls.__name__) + ".json"

        try:
            with open(this_file, mode="r", encoding="utf-8") as new_file:
                string = new_file.read()
                items = Base.from_json_string(string)
                return [cls.create(**dictn) for dictn in items]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes the csv serialization of object into a new file"""
        this_file = cls.__name__ + ".csv"
        with open(this_file, "w", newline="") as new_file:
            if list_objs is None or list_objs == []:
                new_file.write("[]")
            else:
                if cls.__name__ == "Square":
                    keys = ["id", "size", "x", "y"]
                else:
                    keys = ["id", "width", "height", "x", "y"]
                writer = csv.DictWriter(new_file, fieldnames=keys)
                for item in list_objs:
                    writer.writerow(item.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """returns an object from a csv serialized file"""
        this_file = cls.__name__ + ".csv"
        try:
            with open(this_file, "r", newline="") as new_file:
                if cls.__name__ == "Square":
                    key = ["id", "size", "x", "y"]
                else:
                    key = ["id", "width", "height", "x", "y"]
                list_dicts = csv.DictReader(new_file, fieldnames=key)
                list_dicts = [dict([key, int(val)] for key, val in idx.items())
                              for idx in list_dicts]
                return [cls.create(**dictn) for dictn in list_dicts]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draws the indicated shape of the given class"""
        tortilla = turtle.Turtle()
        tortilla.pensize(4)
        tortilla.shape("turtle")
        tortilla.screen.bgcolor("#1969bf")

        tortilla.color("#dcecf7")
        for shape in list_rectangles:
            tortilla.showturtle()
            tortilla.up()
            tortilla.goto(shape.x, shape.y)
            tortilla.down()
            for _ in range(2):
                tortilla.forward(shape.width)
                tortilla.left(90)
                tortilla.forward(shape.height)
                tortilla.left(90)
            tortilla.hideturtle()

        tortilla.color("#edc7ed")
        for shapey in list_squares:
            tortilla.showturtle()
            tortilla.up()
            tortilla.goto(shapey.x, shapey.y)
            tortilla.down()
            for _ in range(2):
                tortilla.forward(shapey.width)
                tortilla.left(90)
                tortilla.forward(shapey.height)
                tortilla.left(90)
            tortilla.hideturtle()

        turtle.exitonclick()
