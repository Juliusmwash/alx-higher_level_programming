#!/usr/bin/python3
""" Define a class 'Square' """


class Square:
    """ Empty 'Square' class """
    def __init__(self, size=0):
        """ Constructor.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """ property method that returns the size of
        the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Property method that sets the value of self.__size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns the area of the square """
        return self.__size * self.__size

    def my_print(self):
        """ Prints the area in form of '#' characters
        For instance, if the area = 10 it will print "##########"
        """
        if self.__size > 0:
            for i in range(self.__size):
                for h in range(self.__size):
                    print("#", end="")
                print("")
        elif self.__size == 0:
            print("")
