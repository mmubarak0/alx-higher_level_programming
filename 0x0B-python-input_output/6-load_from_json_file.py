#!/usr/bin/python3
"""Create object from Json file."""

import json


def load_from_json_file(filename):
    """Json to object converter."""
    with open(filename, encoding="utf-8") as f:
        return json.loads(f.read().rstrip())
