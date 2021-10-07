#!/usr/bin/python3
"""printing square function"""


def print_square(size):
    """print a square with # character
    Args:
        size (int): size of the square
    Raises:
        TypeError: size is not an integer
        ValueError: ize is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for index in range(size):
        [print("#", end="") for j in range(size)]
        print("")
