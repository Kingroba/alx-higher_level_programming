#!/usr/bin/env python3

def raise_exception_msg(message=""):
    raise NameError(message)

# Example usage
try:
    raise_exception_msg("Custom message for the exception")
except NameError as e:
    print("Caught exception:", str(e))

try:
    raise_exception_msg()
except NameError as e:
    print("Caught exception:", str(e))

