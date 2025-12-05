#!/usr/bin/python3
"""
Function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div

    Args:
        matrix: list of lists of integers/floats
        div: number (int or float)

    Raises:
        TypeError: If matrix is not a matrix of numbers
        TypeError: If each row of the matrix is not the same size
        TypeError: If div is not a number
        ZeroDivisionError: If div == 0

    Returns:
        New matrix with elements divided by div and rounded to 2 decimals
    """

    # Validate matrix is list of lists
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate every element + row size consistency
    row_length = None
    for row in matrix:
        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Return new matrix with results
    return [[round(element / div, 2) for element in row] for row in matrix]
