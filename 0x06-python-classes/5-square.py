#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new sqauare.
        Args:
            size (int): The size of the new square.
        """

        self._size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        """Set the size of the square, Validating the input."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """Return the current area of the square."""
        return self._size * self._size

    def my_print(self):
        """Print the sqaure with the # character."""
        for i in range(0, self._size):
            [print("#", end="") for j in range(self._size)]
            print("")
        if self._size == 0:
            print("")
