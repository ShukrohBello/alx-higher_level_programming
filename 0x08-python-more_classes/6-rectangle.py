#!/usr/bin/python3
"""This class defines a Rectangle"""


class Rectangle:
    """Represents a Rectange

    Defining an attribute
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize the data"""
        type(self).number_of_instances += 1
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
        self.__width = valuei

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
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return a string representation of a Rectangle instance
        that is able to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message for every instance of a Rectangle deleted."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
