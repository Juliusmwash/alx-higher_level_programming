#!/usr/bin/python3
"""
Define add_integer function
This functions adds two integer
If float is given it is casted to int before addition
"""


def add_integer(a, b=98):
    """ Function for adding two integers
        a (int) or (float): first parameter.
        b (int) or (float): second parameter. """
    if not isinstance(a, int):
        if not isinstance(a, float):
            raise TypeError("a must be an integer")
    if not isinstance(b, int):
        if not isinstance(b, float):
            raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
