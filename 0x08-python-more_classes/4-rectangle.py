#!/usr/bin/python3
"""This script defines a Rectangle class."""

class Rectangle:
"""Represents a rectangle."""

def __init__(self, width=0, height=0):
    """Initialize a new Rectangle.

    Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """
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
    if value <
