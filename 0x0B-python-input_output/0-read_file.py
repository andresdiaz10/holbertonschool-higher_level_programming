#!/usr/bin/python3
"""Defines a function that reads text from a file"""


def read_file(filename=""):
    """Print the content in the file as UTF-8 text"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
