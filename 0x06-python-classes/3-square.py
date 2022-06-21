#!/usr/bin/python3
"""defining a square based on 2-square.py"""


class Square:
    """defines a square by size"""
    def __init__(self, __size=0):
        """initialize the argument"""
        self.__size = __size
        if not isinstance(__size, int):
            raise TypeError('size must be an integer')

        if __size < o:
            raise ValueError('size must be >= 0')
        """returns the area of a square"""
    def area(self):
        """returns the area of a square"""
        return (salf.__size*self.__size)
