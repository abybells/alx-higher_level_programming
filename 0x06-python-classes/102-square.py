#!/usr/bin/python3
"""Define a square based on 4-square.py"""


class Square:
    """define variables and methods"""

    def __init__(self, size=0):
        """initialize attributes"""
        self.size = size

    @property
    def size(self):
        """getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size"""
        if isinstance(value, int) and value >= 0:
            self.__size = value
        elif not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """define area method, evaluate square area"""
        return self.__size ** 2

        """
        rich comparison methods
        usage: object.__lt__(self, other)
        see: https://docs.python.org/3/reference/datamodel.html
        """

    def __lt__(self, other):
        """less than compare"""
        return self.area() < other.area()

    def __le__(self, other):
        """less or equal compare"""
        return self.area() <= other.area()

    def __eq__(self, other):
        """is equal compare"""
        return self.area() == other.area()

    def __ne__(self, other):
        """is not equal compare"""
        return self.area() != other.area()

    def __gt__(self, other):
        """greater than compare"""
        return self.area() > other.area()

    def __ge__(self, other):
        """greater or equal compare"""
        return self.area() >= other.area()
