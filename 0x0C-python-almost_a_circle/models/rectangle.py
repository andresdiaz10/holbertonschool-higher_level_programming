#!/usr/bin/python3
"""rectangle.py: Define a class rectangle"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init a new rectangle.

        Arguments:
            width (int): width of the rectangle.
            height (int): height of the rectangle
            x (int): coordinate of the rectangle
            y (int): coordinate of the rectangle
            id (int): id of the rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area."""
        return self.width * self.height

    def display(self):
        """print a rectangle using #"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        for y in range(self.y):
            print("")
        for h in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for w in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """Return the representation of the class Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def to_dictionary(self):
        """return a dictionary, representation of the class"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
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
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = index
                elif aux == 1:
                    self.width = index
                elif aux == 2:
                    self.height = index
                elif aux == 3:
                    self.x = index
                elif aux == 4:
                    self.y = index
                aux += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
