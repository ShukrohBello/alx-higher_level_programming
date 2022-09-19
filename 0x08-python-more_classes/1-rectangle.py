#!/usr/bin/python3
"""This class defines a Rectangle"""


class Rectangle:
    """Represents a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize the data"""
        self.width = width
        self.height = height

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
