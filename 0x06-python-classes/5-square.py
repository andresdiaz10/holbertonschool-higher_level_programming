#!/usr/bin/python3
"""square class"""


class Square:
    """square  class"""
    def __init__(self, size=0):
        """init a square

        Args:
            size (int): size of the square
        """

        self.size = size

    @property
    def size(self):
        """get size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return area"""
        return (self.__size * self.__size)

    def my_print(self):
        """print square"""
        for index in range(0, self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
