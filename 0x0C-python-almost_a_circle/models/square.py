#!/usr/bin/python3
""" Defines class 'square' """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class square """
    def __init__(self, size, x=0, y=0, id=None):
        """ class 'Square' constructor """
        super().validator("width", size, 0)
        super().validator("x", 1, x)
        super().validator("y", 1, y)
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ returns a string representation of a square """
        return "[Square] ({:d}) {:d}/{:d} - {:d}\
".format(self.id, self.x, self.y, self.width)
