#!/usr/bin/python3
"""Base geometry."""


class BaseGeometry:
    """Base class."""

    def area(self):
        """Area of the shape."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate integer."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
