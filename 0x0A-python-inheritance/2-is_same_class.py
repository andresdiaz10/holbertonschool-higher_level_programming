#!/usr/bin/python3
"""Define a class checker"""


def is_same_class(obj, a_class):
    """Check if the class is same a given class

    Args:
        obj (any): object to check
        a_class: class to match
    Return:
        if the a_class match True
        otherwise false
    """
    if type(obj) == a_class:
        return True
    return False
