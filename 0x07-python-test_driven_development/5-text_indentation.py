#!/usr/bin/python3
"""Text indentation."""


def text_indentation(text):
    """Print a text with 2 new lines.

    Prints a text with 2 new lines after each of these characters:
    ., ? and:.

    Args:
        text (str): text to modify.
    """
    reserved_characters = [".", "?", ":"]
    is_line_begin = False

    if type(text) is not str:
        raise TypeError("text must be a string")

    for character in text:
        if character in reserved_characters:
            print(character)
            print()
            is_line_begin = True
        else:
            if is_line_begin:
                if character != " ":
                    print(character, end="")
                    is_line_begin = False
            else:
                print(character, end="")
