#!/usr/bin/python3
"""Read file."""


def read_file(filename=""):
    """Read file argument."""
    with open(filename, encoding="utf-8") as f:
        lines = f.read()
        for line in lines:
            print(line, end='')
