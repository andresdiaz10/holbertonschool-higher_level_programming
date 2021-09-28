#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return ([list(map(lambda row: row ** 2, i)) for i in matrix])
