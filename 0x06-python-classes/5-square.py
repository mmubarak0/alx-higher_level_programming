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

    def my_print(self):
        """Print the square with # to stdout."""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()

    @property
    def size(self):
        """Return the private variable size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of private variable size."""
        if type(value) is not int:
            self.__size = 0
            raise TypeError("size must be an integer")
        elif value < 0:
            self.__size = 0
            raise ValueError("size must be >= 0")
        self.__size = value
