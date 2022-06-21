#!/usr/bin/python3
"""defines a square based on 4-square.py"""


class Square:
    """ Initialize class square"""

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

    """Define area of a Square"""
    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print()
        for index in range(self.__size):
            if self.__size != 0:
                print('#' * self.__size)
