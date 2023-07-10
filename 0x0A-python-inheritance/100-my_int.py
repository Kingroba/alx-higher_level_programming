#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""

class MyInt(int):
    """Represents a custom integer class that inverts the equality operators."""

    def __eq__(self, value):
        """Override the == operator to have the opposite behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override the != operator to have the opposite behavior."""
        return self.real == value

