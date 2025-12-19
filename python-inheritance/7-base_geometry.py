#!/usr/bin/python3
"""
This module defines a BaseGeometry class with
an area method and an integer validator.
"""


class BaseGeometry:
    """
    BaseGeometry class that provides geometry validation methods.
    """

    def area(self):
        """
        Raises an Exception indicating that the area method
        is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer greater than 0.

        Args:
            name (str): the name of the value
            value (int): the value to validate
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
