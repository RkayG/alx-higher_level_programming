#!/usr/bin/python3
"""
Module: rectangle.py
Defines a class that inherits from another
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class Constructor
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): horizontal axis
            y (int): vertical axis
            id (int): identity of rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area of rectangle"""
        return self.height * self.width

    def display(self):
        """ displays rectangle with '#' """
        if self.width == 0 or self.height == 0:
            print("")
            return

        for y in range(self.y):
            print('')

        for row in range(self.height):
            for x in range(self.x):
                print(' ', end="")
            for col in range(self.width):
                print('#', end="")
            print('')

    def update(self, *args, **kwargs):
        """
        Update the Rectangle.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes
        """
        if args:
            for ind, val in enumerate(args):
                if ind == 0:
                    self.id = val
                elif ind == 1:
                    self.width = val
                elif ind == 2:
                    self.height = val
                elif ind == 3:
                    self.x = val
                elif ind == 4:
                    self.y = val
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ Returns the dictionary representation of the Rectangle """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
