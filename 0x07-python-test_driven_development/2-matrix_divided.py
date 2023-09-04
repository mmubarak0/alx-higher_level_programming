#!/usr/bin/python3
"""Divide all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divide every item of a matrix with number.

    Args:
        matrix (list(list)): 2d array.
        div (int): integer.
    """
    new_list = []
    len_matrix_row = -1

    # matrix error checking.
    if len(matrix) > 0 and type(matrix[0]) is list:
        len_matrix_row = len(matrix[0])
    else:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
        if len(row) != len_matrix_row:
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # execute the function.
    for idx, row in enumerate(matrix):
        new_list.append([])
        for i in row:
            n = round(i / div, 2)
            new_list[idx].append(n)
    return new_list
