#!/usr/bin/python3
"""Define a function to write inside a file"""


def write_file(filename="", text=""):
    """Write a text in UTF-8 into a file

    Args:
        filename (str): Name of the file.
        text (str): Text to write to the filename
    Return:
        number of characters written
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
