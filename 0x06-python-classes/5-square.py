#!/usr/bin/python3

"""
Define a class Square.

This class represents a square.
"""


class Square:
    """
    Represent a square.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the current area of the square.

        Returns:
            int: The calculated area.
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the '#' character."""
        for i in range(self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
