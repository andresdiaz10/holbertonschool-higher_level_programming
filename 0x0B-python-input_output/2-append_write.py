#!/usr/bin/python3
"""Define a function to append a file"""


def append_write(filename="", text=""):
    """appends a string to the end of File in UTF-8.

    Args:
        filename (str): Name of the file to append.
        text (str): string to append.
    Returns:
        number of character to append.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
