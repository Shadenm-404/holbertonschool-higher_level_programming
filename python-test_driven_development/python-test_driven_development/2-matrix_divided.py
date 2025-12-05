#!/usr/bin/python3
"""
This module defines a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Args:
        matrix: list of lists of integers/floats
        div: number to divide by (int or float)

    Returns:
        A new matrix with elements divided and rounded to 2 decimals

    Raises:
        TypeError: if matrix or div has invalid type
        ZeroDivisionError: if div is zero
    """

    # Validate matrix is list of lists of numbers
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate rows are same size + validate row elements numeric
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Return new divided matrix
    return [[round(item / div, 2) for item in row] for row in matrix]
