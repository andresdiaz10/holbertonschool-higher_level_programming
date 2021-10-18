#!/usr/bin/python3
"""base.py: Define a base model for geometric objects"""
import json
import csv
import turtle


class Base:
    """Base model for all geometrics classes

    base of all other classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Init a new base object

        Arguments:
            id (int): id of the new base object
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """return a json"""
        if list_dictionaries == [] or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                tmp = [index.to_dictionary() for index in list_objs]
                file.write(Base.to_json_string(tmp))

    @staticmethod
    def from_json_string(json_string):
        """that returns the list of the JSON string representation"""
        if json_string == "[]" or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """that returns an instance with all attributes already set"""
        if dictionary != {} and dictionary:
            if cls.__name__ == "Square":
                new_obj = cls(1)
            else:
                new_obj = cls(1, 1)
            new_obj.update(**dictionary)
            return new_obj

    @classmethod
    def load_from_file(cls):
        """that returns a list of instances:"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                tmp = Base.from_json_string(file.read())
                return [cls.create(**index) for index in tmp]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """write in to csv file"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            if list_objs == [] or list_objs is None:
                file.write("[]")
            else:
                if cls.__name__ == "Square":
                    rownames = ["id", "size", "x", "y"]
                else:
                    rownames = ["id", "width", "height", "x", "y"]
                aux = csv.DictWriter(file, rownames=rownames)
                for index in list_objs:
                    aux.writerow(index.to_dictionary())

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draw the geometric figure"""
        window = turtle.Turtle()
        window.screen.bgcolor("#000000")
        window.pensize(5)
        window.color("#FFFFFF")
        for rectangle_class in list_rectangles:
            window.up()
            window.goto(rectangle_class.x, rectangle_class.y)
            window.down()
            for index in range(2):
                window.forward(rectangle_class.width)
                window.left(90)
                window.forward(rectangle_class.height)
                window.left(90)
        window.color("#FFC0CB")
        for square_class in list_squares:
            window.up()
            window.goto(square_class.x, square_class.y)
            window.down()
            for index in range(2):
                window.forward(square_class.width)
                window.right(90)
                window.forward(square_class.height)
                window.right(90)
        turtle.exitonclick()
