#!/usr/bin/python3
""" Define a class Square"""


class Square:
    """A class Square
    Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0):
    size must be an integer, otherwise raise a TypeError exception
    with the message size must be an integer
    if size is less than 0, raise a ValueError exception
    with the message size must be >= 0
    """

    def __init__(self, size=0):
        """Initializes a square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
