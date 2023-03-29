#!/usr/bin/python3
""" Define a class 'Square' """


class Square:
    """ Empty 'Square' class """
    def __init__(self, size=0):
        """ Constructor.

        Args:
            size (int): The size of the square.
        
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        """
        try:
            if size < 0:
                raise ValueError
            if not isinstance(size, int):
                raise TypeError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
        else:
            self.__size = size
