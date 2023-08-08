#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = []
    for idx, char in enumerate(str):
        if idx != n:
            new_str.append(char)
    return "".join(new_str)
