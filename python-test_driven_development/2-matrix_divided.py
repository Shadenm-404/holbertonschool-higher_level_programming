#!/usr/bin/python3
"""
This module defines a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix: list of lists of integers/floats
        div: number (int or float) to divide by

    Returns:
        A new matrix with each element divided and rounded to 2 decimals

    Raises:
        TypeError: if matrix format is invalid or div is not a number
        ZeroDivisionError: if div is zero
    """

    # Validate matrix
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate each element and check row size consistency
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Return new divided matrix
    return [[round(item / div, 2) for item in row] for row in matrix]
