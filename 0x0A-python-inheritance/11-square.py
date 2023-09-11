#!/usr/bin/python3
"""Base geometry."""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square shape."""

    def __init__(self, size):
        """Init Squre instance."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Shape area."""
        return self.__size ** 2

    def __str__(self):
        """Str represntation of rectangle."""
        return f"[Square] {self.__size}/{self.__size}"
