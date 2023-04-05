#!/usr/bin/python3
"""
Define function print_square
This function prints a square using character '#'
"""


def print_square(size):
    """ Prints a square """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
            if j == size - 1:
                print("")
