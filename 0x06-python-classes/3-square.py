#!/usr/bin/python3
"""defining a square based on 2-square.py"""


class Square:
    """defines a square by size"""
    def __init__(self, __size=0):
        if type(__size) is not int:
            raise TypeError("size must be an integer")
        elif __size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = __size

    """Return area of Square object"""
    def area(self):
        return (self.__size * self.__size)
