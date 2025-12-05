#!/usr/bin/python3
"""
Function that divides all elements of a matrix by a number.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by `div`.
    Args:
        matrix (list): A list of lists of integers/floats.
        div (int/float): The number to divide by.
    Returns:
        list: A new matrix where each value is divided and rounded to 2 decimals.
    Raises:
        TypeError: If matrix is not a list of lists of numbers.
        TypeError: If rows of the matrix are not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.
    """

    # Validate matrix type
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(x, (int, float))
                    for row in matrix for x in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate equal row size
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Return new divided matrix
    return [[round(x / div, 2) for x in row] for row in matrix]
