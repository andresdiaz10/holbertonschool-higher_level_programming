#!/usr/bin/python3
"""Define a class and inhertid checker"""


def inherits_from(obj, a_class):
    """Check if the object is an inherited of a given class

    Args:
        obj (any): object to check
        a_class: class to match
    Return:
        if the a_class is an inherited True
        otherwise false
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
