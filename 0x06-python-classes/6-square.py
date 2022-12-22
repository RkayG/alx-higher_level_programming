#!/usr/bin/python3
"""
Module 6-square
Defines class Square with private
attribute size
"""


class Square:
    """ Square class

        Functions:
            __init__(self, size, position)
            area(self)
            size(self, value)
            position(self)
            position(self, value)
            area(self)
            my_print(self)
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes square
        Attributes:
            size(int): size of a side of square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter

        retrieves private atrribute 'size'
        """
        return self.__position

    @size.setter
    def position(self, value):
        """
        sets value of private attribute 'size'
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints square with '#' character
        """
        if self.__size == 0:
            print("")
            return
        else:
            print("\n" * self.__position[1], end='')
            for i in range(0, self.__size):
                for j in range(0, self.__position[0]):
                    print(" ", end='')
                for k in range(0, self.__size):
                    print("#", end='')
                print("")
