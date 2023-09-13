#!/usr/bin/python3
"""Append to a file."""


def append_write(filename="", text=""):
    """Append write to file."""
    with open(filename, "a", encoding="utf-8") as f:
        n = f.write(text)
    return n
