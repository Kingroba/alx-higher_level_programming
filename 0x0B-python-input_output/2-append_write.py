#!/usr/bin/python3
"""This code snippet defines file-related functions."""

def read_file(filename=""):
    """This function reads the contents of a UTF8 text file and prints them to the standard output."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

def write_file(filename="", text=""):
    """This function writes a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to be written to the file.
    Returns:
        The count of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

def append_write(filename="", text=""):
    """This function appends a string to the end of a UTF8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to be appended to the file.
    Returns:
        The count of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
