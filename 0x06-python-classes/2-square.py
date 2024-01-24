#!/usr/bin/python3
"""Define a class Sqaure."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.__size = size
        self._validate_size()

    def _validate_size(self):
        """Validate the size attribute."""
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
