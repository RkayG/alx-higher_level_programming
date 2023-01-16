#!/usr/bin/python3
"""
Module: square.py
Defines a square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ class constructor
        Args:
            size: size of square
            x: horizontal axis
            y: vertical axis
            id: identity of square
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size Getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the Square.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents sizw attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes
        """
        if args:
            for ind, val in enumerate(args):
                if ind == 0:
                    self.id = val
                elif ind == 1:
                    self.size = val
                elif ind == 2:
                    self.x = val
                elif ind == 3:
                    self.y = val
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ Returns the dictionary representation of the Square """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
            }

    def __str__(self):
        """Return the print() and str() representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)
