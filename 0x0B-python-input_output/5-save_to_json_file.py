#!/usr/bin/python3
"""Define a function that writes JSON to a file."""
import json


def save_to_json_file(my_obj, filename):
    """Write a object to a file using JSON."""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
