#!/usr/bin/python3
"""define a class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Init a square object

        Square class
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the object"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """return a representation of the object."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y,
                                                 self.width)
