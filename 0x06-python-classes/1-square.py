#!/usr/bin/python3
""" Define a class Square"""


class Square:
    """ This class defines a square
        Private instance attribute: size
        Instantiation with size (no type/value verification)
    """

    def __init__(self, size):
        """Initializing the data"""
        self._size = size
