#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """

        self.width = width
        self.height = height

        @property
        def width(self):
            """Get/set the width of the rectangle."""
            return self.__width

        @width.setter
        def width(self, value):
            self.validate_dimension(value, "width")
            self.__width = value

        @property
        def height(self):
            """Get/set the height of the rectangle."""
            return self.__height

        @height.setter
        def height(self, value):
            self.validate_dimension(value, "height")
            self.__height = value

        def __str(self):
            """Return a string respresentation of the rectangle."""
            return "[Rectangle] {}/{}".format(self.width, self.height)
