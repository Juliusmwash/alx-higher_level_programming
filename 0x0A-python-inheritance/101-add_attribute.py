#!/usr/bin/python3
""" Defines the function 'add_attribute' """


def add_attribute(obj, value, value1):
    """ Adds an attribute to an object """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, value, value1)
