#!/usr/bin/python3
"""Define a class and inhertid checker"""


def is_kind_of_class(obj, a_class):
    """Check if the object is an inherited of a given class

    Args:
        obj (any): object to check
        a_class: class to match
    Return:
        if the a_class is an inherited True
        otherwise false
    """
    if isinstance(obj, a_class):
        return True
    return False
