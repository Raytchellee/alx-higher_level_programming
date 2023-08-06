#!/usr/bin/python3
"""Function for matrix element division"""


def matrix_divided(matrix, div):
    """Returns divided elements of matrix

    Args:
        matrix: list of list of dividends
        div: divisor
    Returns:
        The divided elements of matrix in a new matrix
    """

    if (type(matrix) is not list or len(matrix) == 0 or
            not all(type(row) is list for row in matrix) or
            not all((type(val) is int or type(val) is float)
                    for val in [item for row in matrix for item in row])):
        raise TypeError("matrix must be a matrix (list of lists) of"
                        " integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not float and type(div) is not int:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
