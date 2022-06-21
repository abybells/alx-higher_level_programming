#!/usr/bin/python3
"""Define a square based on 5-square.py"""


class Square:
    """Initialize the square"""

    def __init__(self, __size=0, position=(0, 0)):
        self.__size = size
        self.position = position
        if type(__size) is not int:
            raise TypeError("size must be an integer")
        if __size < 0:
            raise ValueError("size must be >= 0")


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size * self.__size)

    @property
    def position(self):
        return self.position

    @positon.setter
    def position(self, size):
        if type(size) is not tuple or len(size) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(size[0]) is not int or type(size[1] is not int:
                raise TypeError("position must be a tuple of 2 positive integers")
                if size[0] < 0 or size[1] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
                self.position = size

    def my_print(self):
    if self.__size == 0:
    print()
    else:
    for index in range(self.position[1]):
    print()
    for index in range(self.__size):
    print("{}{}".format(" " * self.position[0], "#" * self.__size))
