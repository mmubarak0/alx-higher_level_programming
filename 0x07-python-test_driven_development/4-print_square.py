#!/usr/bin/python3
"""Print Squares."""


def print_square(size):
    """Print Square shape.

    Args:
        size (int): square size.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
