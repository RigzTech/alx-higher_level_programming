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

    @property
    def size(self):
        """getter"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """class method
        returns the current square area
        """
        return int(self.__size) * int(self.__size)
