#!/usr/bin/python3
"""
Module 4-square
Defines class Square with private
attribute size
"""


class Square:
    """ Square class

        Functions:
            __init__(self, size)
            area(self)
            size(self)
            size(self, value)
            area(self)
    """

    def __init__(self, size=0):
        """
        Initializes square
        Attributes:
            size(int): size of a side of square
        """
        self.size = size

    @property
    def size(self):
        """
        Getter

        retrieves private atrribute 'size'
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets value of private attribute 'size'
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Returns the current square area
        """
        return self.__size ** 2
