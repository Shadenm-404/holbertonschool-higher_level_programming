#!/usr/bin/python3
"""
Defines a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all matrix elements by div and returns a new matrix

    Args:
        matrix (list of lists): Matrix containing integers/floats
        div (int/float): Number divisor

    Raises:
        TypeError: matrix is not a list of lists of numbers
        TypeError: rows not equal size
        TypeError: div is not a number
        ZeroDivisionError: div == 0

    Returns:
        list: new matrix with elements divided by div
    """

    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_len = None
    for row in matrix:
        if row_len is None:
            row_len = len(row)
        elif len(row) != row_len:
            raise TypeError(
                "Each row of the matrix must have the same size"
            )

        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists)"
                    " of integers/floats"
                )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [
        [round(elem / div, 2) for elem in row]
        for row in matrix
    ]
