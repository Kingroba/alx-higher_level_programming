#!/usr/bin/python3

import sys


def execute_safely(function, *arguments):
    """Executes a function safely.

    Args:
        function: The function to execute.
        arguments: Arguments for the function.

    Returns:
        If an error occurs - None.
        Otherwise - the result of the function call.
    """
    try:
        result = function(*arguments)
        return result
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None


# Example usage
def add_numbers(a, b):
    return a + b


def divide_numbers(a, b):
    return a / b


result1 = execute_safely(add_numbers, 5, 10)
print("Result 1:", result1)

result2 = execute_safely(divide_numbers, 10, 0)
print("Result 2:", result2)

