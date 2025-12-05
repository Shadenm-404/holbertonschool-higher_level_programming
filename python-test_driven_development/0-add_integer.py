#!/usr/bin/python3
"""
This module provides a function that adds two numbers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result as an integer.

    Args:
        a: first number (int or float)
        b: second number (int or float), default is 98

    Returns:
        The sum of a and b after casting to int

    Raises:
        TypeError: if a or b are not int or float
    """

    # Handle NaN or None explicitly
    if a is None or (isinstance(a, float) and a != a):
        raise TypeError("a must be an integer")
    if b is None or (isinstance(b, float) and b != b):
        raise TypeError("b must be an integer")

    # Handle invalid types
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
