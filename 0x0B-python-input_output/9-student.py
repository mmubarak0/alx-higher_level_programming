#!/usr/bin/python3
"""Studen to json."""


class Student:
    """Student class."""

    def __init__(self, first_name, last_name, age):
        """Init the student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Convert to json."""
        return self.__dict__
