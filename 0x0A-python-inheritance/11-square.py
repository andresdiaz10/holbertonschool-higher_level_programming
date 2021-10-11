#!/usr/bin/python3
"""Definition of a Square that inherits form Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A square """

    def __init__(self, size):
        """Init a square

        Args:
            size (int): size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
