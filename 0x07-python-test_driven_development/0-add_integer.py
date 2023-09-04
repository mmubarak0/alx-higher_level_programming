#!/usr/bin/python3
"""Adds two integers.

This function takes two parameters
Return their sum.
"""


def add_integer(a, b=98):
    """Add function return the sum of a + b.

    Args:
        a (int): first number.
        b (int): second number.
    """
    if type(a) is int or type(a) is float:
        if type(b) is int or type(b) is float:
            return int(a) + int(b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
    return 0


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
