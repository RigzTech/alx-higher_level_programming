#!/usr/bin/python3
"""class of a square"""


class Square:
    """attributes"""
    def __init__(self, size=0):
        """instance attributes
        size: @private size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
