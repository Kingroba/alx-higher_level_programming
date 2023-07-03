#!/usr/bin/python3
"""This script defines a Rectangle class.

Attributes:
    number_of_instances (int): The number of instances of the Rectangle class.
"""

number_of_instances = 0

def __init__(self, width=0, height=0):
    """Initialize a new Rectangle.

    Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """
    type(self).number_of_instances += 1
    self._width = width
    self._height = height

@property
def width(self):
    """Get or set the width of the Rectangle."""
    return self._width

@width.setter
def width(self, value):
    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueError("width must be >= 0")
    self._width = value

@property
def height(self):
    """Get or set the height of the Rectangle."""
    return self._height

@height.setter
def height(self, value):
    if not isinstance(value, int):
        raise TypeError("height must be an integer")
    if value < 0:
        raise ValueError("height must be >= 0")
    self._height = value

def area(self):
    """Return the area of the Rectangle."""
    return self._width * self._height

def perimeter(self):
    """Return the perimeter of the Rectangle."""
    if self._width == 0 or self._height == 0:
        return 0
    return 2 * (self._width + self._height)

def __str__(self):
    """Return a string representation of the Rectangle.

    The rectangle is represented using the '#' character.
    """
    if self._width == 0 or self._height == 0:
        return ""

    rect = []
    for i in range(self._height):
        rect.extend(['#' for j in range(self._width)])
        if i != self._height - 1:
            rect.append("\n")
    return "".join(rect)

def __repr__(self):
    """Return a string representation of the Rectangle."""
    return f"Rectangle({self._width}, {self._height})"

def __del__(self):
    """Print a message when a Rectangle instance is deleted."""
    type(self).number_of_instances -= 1
    print("Bye rectangle...")

