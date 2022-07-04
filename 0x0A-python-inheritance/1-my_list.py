#!/usr/bin/python3
"""
module of class MyList that inherits from list
"""


class MyList(list):
    """
    Subclass that inherits from class list
    """
    def print_sorted(self):
        """print the list, but sorted in ascending order"""
        return print(sorted(self))
