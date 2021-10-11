#!/usr/bin/python3
"""Define a BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry"""

    def area(self):
        """None"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a value as integer

        Args:
            name (str): name of the parameter
            value (int): value to validates
        Raises:
            ValueError: if value is <=0
            TypeEor: if the value is not an int
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
