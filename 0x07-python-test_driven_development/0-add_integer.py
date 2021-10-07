#!/usr/bin/python3
"""A function that adds 2 integers"""


def add_integer(a, b=98):
    """Return the add of a and b.

    Raises:
        TypeError: When either of a or b is a non integer or float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
