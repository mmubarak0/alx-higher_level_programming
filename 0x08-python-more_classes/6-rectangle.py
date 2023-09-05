#!/usr/bin/python3
"""Rectangle class."""


class Rectangle:
    """A rectangle class."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize the rectangle instance."""
        Rectangle.number_of_instances += 1
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @width.setter
    def width(self, width):
        """Setter for width."""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """Setter for height."""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """Rectangle area."""
        return self.__height * self.__width

    def perimeter(self):
        """Rectangle perimeter."""
        if self.__height and self.__width:
            return 2 * (self.__height + self.__width)
        return 0

    def __str__(self):
        """Return the string representation of rectangle."""
        result = ""
        if self.__height and self.__width:
            res = []
            for i in range(self.__height):
                res.append("#" * self.__width)
            result = "\n".join(res)
        return result

    def __repr__(self):
        """Return the string repr of an instance of the class."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Call when an instance is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
