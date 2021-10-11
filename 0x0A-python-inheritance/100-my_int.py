#!/usr/bin/python3
"""Class MyInt."""


class MyInt(int):
    """invert operators"""

    def __eq__(self, value):
        """invert == operator"""
        return self.real != value

    def __ne__(self, value):
        """invert != operator"""
        return self.real == value
