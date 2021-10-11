#!/usr/bin/python3
"""Define a class rectangle that inherits from basegeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Init a new rectangle

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area """
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description."""
        description = "[" + str(self.__class__.__name__) + "] "
        description += str(self.__width) + "/" + str(self.__height)
        return description
