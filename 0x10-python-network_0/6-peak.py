#!/usr/bin/python3
"""Find the peak element."""


def find_peak(arr):
    """Find peak."""
    prev = -float("inf")
    if len(arr) == 0:
        return None
    for idx, value in enumerate(arr):
        next = arr[idx + 1] if idx < len(arr) - 1 else -float("inf")
        if prev <= value >= next:
            return value
            break
        prev = value
