#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elements of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    ret = 0  # Initialize counter variable to keep track of printed elements
    for i in range(x):  # Iterate x times
        try:
            print("{}".format(my_list[i]), end="")  # Print element at index i
            ret += 1  # Increment counter for successfully printed elements
        except IndexError:  # Handle index out of range error
            break  # Exit loop if index is out of range
    print("")  # Print empty string to add newline character
    return ret  # Return the count of elements printed

