#!/usr/bin/python3
"""Write an empty class Square that defines a square."""


class Square:
    """empty square class."""

    def __init__(self, size=0):
        """Initialize the square instance.

        Args:
            size (int): square size.
        """
        if type(size) is not int:
            self.__size = 0
            raise TypeError("size must be an integer")
        elif size < 0:
            self.__size = 0
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
