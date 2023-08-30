#!/usr/bin/python3
"""Write an empty class Square that defines a square."""


class Square:
    """empty square class."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square instance.

        Args:
            size (int): square size.
            position (tuple(int, int)): square position.
        """
        if type(size) is not int:
            self.__size = 0
            raise TypeError("size must be an integer")
        elif size < 0:
            self.__size = 0
            raise ValueError("size must be >= 0")
        self.__size = size
        if type(position) is not tuple:
            self.__position = (0, 0)
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            self.__position = (0, 0)
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int or type(position[1]) is not int:
            self.__position = (0, 0)
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            self.__position = (0, 0)
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with # to stdout."""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            for j in range(self.__size):
                print("#", end="")
            print()

    @property
    def size(self):
        """Return the private variable size."""
        return self.__size

    @property
    def position(self):
        """Return the private variable size."""
        return self.__position

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

    @position.setter
    def position(self, value):
        """Set the value of private variable position."""
        if type(value) is not tuple:
            self.__position = (0, 0)
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            self.__position = (0, 0)
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            self.__position = (0, 0)
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            self.__position = (0, 0)
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __str__(self):
        if self.__size == 0:
            return ""
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            for j in range(self.__size):
                print("#", end="")
            if (i < self.__size - 1):
                print()
        return ""
