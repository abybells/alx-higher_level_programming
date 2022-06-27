#!/usr/bin/python3
"""This module defines a rectangle by 0-rectangle.py"""


class Rectangle:
    """Initialize rectangle with height and width"""

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """getter for rectangle width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
