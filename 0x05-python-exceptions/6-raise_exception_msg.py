#!/usr/bin/env python3

def raise_exception_msg(message=""):
    """
    Raise a NameError exception with a message.

    Args:
        message (str): The error message to be displayed. Defaults to an empty string.
        
    Raises:
        NameError: An exception indicating that a name is not found.
    """
    raise NameError(message)
