#!/usr/bin/python3
"""This code snippet presents a function for reading the contents of a text file."""

def read_file(filename=""):
"""This function reads a UTF8 text file and prints its contents to the standard output."""
with open(filename, encoding="utf-8") as f:
print(f.read(), end="")
