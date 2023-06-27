#!/usr/bin/python3

"""
Define a class Square.

This class represents a square.
"""


class Square:
    """
    Represent a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
