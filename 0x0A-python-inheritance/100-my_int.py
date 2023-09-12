#!/usr/bin/python3
"""My Integer."""


class MyInt(int):
    """Myint class."""

    def __eq__(self, obj):
        """Equality method."""
        return (self - obj) != 0

    def __ne__(self, obj):
        """Inequality metho."""
        return (self - obj) == 0
