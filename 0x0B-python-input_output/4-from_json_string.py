#!/usr/bin/python3
"""From JSON to python."""

import json


def from_json_string(my_str):
    """Json to python converter."""
    return json.loads(my_str)
