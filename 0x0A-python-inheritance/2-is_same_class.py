#!/usr/bin/python3
"""Defines a function for checking if an object is an instance of a specific class."""

def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare the object's type to.

    Returns:
        True if the object is exactly an instance of the specified class,
        otherwise False.
    """
    if type(obj) == a_class:
        return True
    return False

