#!/usr/bin/python3
"""Defines a function for checking if an object is an inherited instance of a class."""

def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare the object's type to.

    Returns:
        True if the object is an inherited instance of the specified class,
        otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

