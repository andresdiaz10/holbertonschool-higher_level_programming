#!/usr/bin/python3
"""A matrix division function"""


def matrix_divided(matrix, div):
    """Div all element a matrix

    Args:
        matrix (list): a matrix with ints
        div (float/int) = divisor.
    Raises:
        TypeError: if the matrix contains no numbers.
        TypeError: if the matrix contains rows of different sizes
        TypeError: if div is not an int or float
        ZeroDivisionError: if div is zero
    Returns:
        result of the division
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if (matrix == [] or not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(element, float) or isinstance(element, int))
                    for element in [n for row in matrix for n in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
