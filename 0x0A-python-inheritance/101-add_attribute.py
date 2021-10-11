#!/usr/bin/python3
"""function add attributes"""


def add_attribute(objec, attribute, value):
    """add a new attribute to an object

    Args:
        objec (any): object to add attribute
        attribute (any): name of the attribute
        value (any): value of the attribute
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(objec, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(objec, attribute, value)
