#!/usr/bin/python3
"""base.py: Define a base model for geometric objects"""
import json


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
