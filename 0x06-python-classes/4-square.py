#!/usr/bin/python3
"""defining a square based on 3-square.py"""


class Square:
    """defines a square by size"""
    def __init__(self, __size=0):
        self.__size = __size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """Return the current square area"""
    def area(self):
        return (sel.__size * self.__size)
