#!/usr/bin/python3
"""Define a function convert JSON to object."""
import json


def from_json_string(my_str):
    """return the object representation of a JSON."""
    return json.loads(my_str)
