#!/usr/bin/python3
"""Class to Json."""

import json


def class_to_json(obj):
    """Class to json object."""
    return obj.__dict__
