#!/usr/bin/python3
"""
This module defines a BaseGeometry class.
"""


class BaseGeometry:
    """
    BaseGeometry class.
    """

    def area(self):
        """
        Raises an Exception with a specific message.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer greater than 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
