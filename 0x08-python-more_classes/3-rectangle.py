#!/usr/bin/python3
"""This class defines a Rectangle"""


class Rectangle:
    """Represents a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize the data"""
        self.width = width
        self.height = height

    def __str__(self):
        """Returns"""
        if self.__height == 0 or self._width == 0:
            return ""
        rect = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rect += "#"
            rect += "\n"
        return rect[:-1]

    @property
    def width(self):
        """Retrieves the property"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width to a value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves (get) the property"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of a square"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of a square"""
        if self.__width == 0 or self.__height == 0:
            return (0)

        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
    """Prints the character #"""
       if self.__width == 0 or self._height == 0:
            return ""
        rect = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rect += "#"
            rect += "\n"
        return rect[:-1]

