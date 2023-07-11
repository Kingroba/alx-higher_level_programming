#!/usr/bin/python3
"""This code snippet defines a function for generating Pascal's Triangle."""

def pascal_triangle(n):
    """Generate Pascal's Triangle of size n.

    Args:
        n (int): The size of the Pascal's Triangle.

    Returns:
        list: A list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        previous_row = triangle[-1]
        new_row = [1]
        for i in range(len(previous_row) - 1):
            new_row.append(previous_row[i] + previous_row[i + 1])
        new_row.append(1)
        triangle.append(new_row)
    return triangle
