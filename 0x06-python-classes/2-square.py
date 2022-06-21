#!/usr/bin/python3
"""defines a class square based on 1-square.py"""


class Square:
    """initializing size as an argument"""
    def __init__(self, __size=0):
        """initializing new square with the __size argument"""
        self.__size = __size
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
