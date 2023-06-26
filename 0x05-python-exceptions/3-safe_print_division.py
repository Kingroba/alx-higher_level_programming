#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Returns the division of a by b.

    Args:
        a: The numerator.
        b: The denominator.

    Returns:
        The result of the division or None if there's an error.
    """
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return div

