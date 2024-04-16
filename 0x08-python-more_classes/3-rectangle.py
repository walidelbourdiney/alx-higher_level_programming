#!/usr/bin/python3

"""This is a define of Rectangle"""


class Rectangle:
    """Rectangle"""
    def __init__(self, width=0, height=0):
    """Initalize the rectangle.

    Args:
        width (int): rectangle width
        height (int): rectangle height
    """
    self.height = height
    self.width = width

    @property
    def width(self):
        """Return the width value."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the rectangle width

        Args:
            value (int): rectangle width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the rectangle height.

        Args:
            value (int): Rectangle new height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

                                                                                                                                                def area(self):
        """Return: Rectangle area."""
        return self.__height * self.__width

                                                                                                                                                def perimeter(self):
        """Return: Rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Prints the rectangle with the character"""
        temp = ""
        if self.__width == 0 or self.__height == 0:
            return temp
        for i in range(self.__height):
            for j in range(self.__width):
                temp += "#"
            if i != self.__height - 1:
                temp += "\n"
        return temp
