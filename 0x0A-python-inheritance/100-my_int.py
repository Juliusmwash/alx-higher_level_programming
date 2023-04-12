#!/usr/bin/python3
""" Defines class MyInt that inherits fron class int """


class MyInt:
    """ reverses the comparison signs """
    def __init__(self, num):
        """ class MyInt constructor """
        self.num = num

    def __eq__(self, value):
        """ reverses the '==' sign """
        return not self.num

    def __str__(self):
        """ return an string """
        return "{:d}".format(self.num)
