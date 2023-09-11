#!/usr/bin/python3
"""Class MyList that inherits from list."""


class MyList(list):
    """Mylist custom list."""

    def print_sorted(self):
        """Print my list."""
        print(sorted(self))
