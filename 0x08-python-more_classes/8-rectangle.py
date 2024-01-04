#!/usr/bin/python3
"""
defines a rectangle
"""


class Rectangle:
    """rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """instantiation"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width"""
        self.__width = value
        try:
            assert type(self.__width) == int
        except BaseException:
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        self.__height = value
        try:
            assert type(self.__height) == int
        except BaseException:
            raise ValueError("height must be >= 0")

    def area(self):
        """returns the area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """print rectangle using #"""
        if self.__width == 0 or self. __height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                print(Rectangle.print_symbol, end="")
            print()
        return ""

    def __repr__(self):
        """repr method to enable create new instance using #"""
        return "Rectangle(" + str(self.__width) +
            ", " + str(self.__height) + ")"

    def __del__(self):
        """delete a rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """return biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
