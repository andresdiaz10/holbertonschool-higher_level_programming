#!/usr/bin/python3
"""Define a list class MyList"""


class MyList(list):
    """Do a sorted printing"""

    def print_sorted(self):
        """Print a list in ascending order"""
        print(sorted(self))
