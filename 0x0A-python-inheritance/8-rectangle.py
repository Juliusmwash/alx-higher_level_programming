#!/usr/bin/python3
""" Defines class 'BaseGeometry' """


class BaseGeometry:
    """ Contains some arithmetic operations """
    def area(self):
        """ Computes area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ inherits from BaseGeometry class """
    def __init__(self, width, height):
        """ class rectangle constructor """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
