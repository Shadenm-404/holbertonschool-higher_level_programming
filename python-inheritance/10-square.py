#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class.
    """

    def __init__(self, size):
        """
        Initialize a Square with size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
