#!/usr/bin/python3
"""New Class Square"""


class Square:
    """ Aclass Square that defines a square by: (based on 0-square.py)"""
    def _init_(self, size=0):
        """Initialize square with the size"""
        self.__size = size

        def area(self):
            """Public instance method that returns the current square area"""
            return self._size * self._size

        @property
        def size(self):
            """Method to retrieve"""
            return self.__size

        @size.setter
        def size(self, value):
            """Setter method"""
            self.__size = value

            """ Exception with the message"""
            if type(value) is not int:
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
