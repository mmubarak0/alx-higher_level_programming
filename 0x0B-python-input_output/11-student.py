#!/usr/bin/python3
"""Studen to json."""


class Student:
    """Student class."""

    def __init__(self, first_name, last_name, age):
        """Init the student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Convert to json."""
        if type(attrs) is list and len(attrs) > 0:
            new_dict = {}
            if all(type(s) is str for s in attrs):
                for s in attrs:
                    if s in self.__dict__:
                        new_dict[s] = self.__dict__[s]
                if len(new_dict) > 0:
                    return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes."""
        for i, j in json.items():
            setattr(self, i, j)
