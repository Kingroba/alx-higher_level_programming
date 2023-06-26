#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """
    Safely prints an integer using "{:d}".format().

    If a ValueError or TypeError occurs while printing the integer,
    it catches the exception and prints an error message to the
    standard error stream.

    Args:
        value (int): The integer to print.

    Returns:
        bool: True if the integer is printed successfully, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False


# Testing the function
value = 42
print("Printing value:", value)
result = safe_print_integer_err(value)
print("Print successful:", result)

value = "invalid"
print("Printing value:", value)
result = safe_print_integer_err(value)
print("Print successful:", result)

