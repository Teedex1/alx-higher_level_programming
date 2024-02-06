#!/usr/python3
"""Defines a file-appending function."""

def append_write(filename="", text=""):
    """Appends a string to the end of the a UTF8 text file.

    Args:
        filename (str): The name of the field to append to.
        text (str): The string to append to the file.
    Reasons:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

