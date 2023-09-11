#!/usr/bin/python3
"""Base geometry."""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle shape."""

    def __init__(self, width, height):
        """Initialize a base geometry."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
        super().__init__()
