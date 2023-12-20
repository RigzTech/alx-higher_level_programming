#!/usr/bin/python3
"""class of a square"""


class Square:
    """attributes"""
    def __init__(self, size=0, position=(0, 0)):
        """instance attributes
        size: @private size of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """postion getter"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """position setter"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """class method
        returns the current square area
        """
        return int(self.__size) * int(self.__size)

    def my_print(self):
        """print the square in (#)"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
