#!/usr/bin/python3
"""This code defines a function for performing object attribute lookup."""

def lookup(obj):
"""This function returns a list of available attributes for a given object."""
return dir(obj)
