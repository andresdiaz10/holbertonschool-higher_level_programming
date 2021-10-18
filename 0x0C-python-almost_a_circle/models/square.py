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

    def to_dictionary(self):
        """return a dictonary of the class"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def update(self, *args, **kwargs):
        """update attributes of the class"""
        if args and len(args) != 0:
            aux = 0
            for index in args:
                if aux == 0:
                    if index is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = index
                elif aux == 1:
                    self.size = index
                elif aux == 2:
                    self.x = index
                elif aux == 3:
                    self.y = index
                a += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
