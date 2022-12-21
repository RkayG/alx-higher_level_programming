#!/usr/bin/python3
"""
Module 3-square
Defines class Square with private
attribute size
"""


class Square:
    """ Square class

        Functions:
            __init__(self, size)
            area(self)
    """

    def __init__(self, size=0):
        """
        Initializes square
        Attributes:
            size(int): size of a side of square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size musr be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Returns the current square area
        """
        return self.__size ** 2
