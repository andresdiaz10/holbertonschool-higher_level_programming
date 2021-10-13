#!/usr/bin/python3
"""Define a function that read JSON file."""
import json


def load_from_json_file(filename):
    """Create a object from JSON file."""
    with open(filename) as file:
        return json.load(file)
