#!/usr/bin/python3
"""
This module provides a function to add two integers.
"""


def add_integer(a, b=98):
    """
    Returns the addition of two integers.

    Args:
        a: first number (int or float)
        b: second number (int or float), default = 98

    Raises:
        TypeError: if a or b is not int or float,
                   or if it’s a float NaN value

    Returns:
        int: the result of a + b
    """
    import math

    # Validate a
    if not isinstance(a, (int, float)) or (isinstance(a, float) and math.isnan(a)):
        raise TypeError("a must be an integer")

    # Validate b
    if not isinstance(b, (int, float)) or (isinstance(b, float) and math.isnan(b)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
