#!/usr/bin/python3
"""base.py: Define a base model for geometric objects"""


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
