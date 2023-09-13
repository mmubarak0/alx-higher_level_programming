#!/usr/bin/python3
"""Write to file."""


def write_file(filename="", text=""):
    """Write to file."""
    with open(filename, "w", encoding="utf-8") as f:
        n = f.write(text)
    return n
