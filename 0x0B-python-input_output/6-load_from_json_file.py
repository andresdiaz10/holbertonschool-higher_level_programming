#!/usr/bin/python3
"""Define a function that read JSON file."""


def load_from_json_file(filename):
    """Create a object from JSON file."""
    with open(filename, "r") as file:
        return json.load(file.read())
