#!/usr/bin/python3
"""
This module defines a BaseGeometry class with
an area method that is not implemented.
"""


class BaseGeometry:
    """
    BaseGeometry class with an unimplemented area method.
    """

    def area(self):
        """
        Raises an Exception indicating that the area method
        is not implemented.
        """
        raise Exception("area() is not implemented")
