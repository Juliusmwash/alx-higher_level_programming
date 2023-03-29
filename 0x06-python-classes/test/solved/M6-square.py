#!/usr/bin/python3
class Square1:
    def __init__(self, size=0, position=(0, 0)):
        if size < 0:
            raise ValueError("size must be greater than 0")
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        if len(position) < 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in range(2):
            if position[i] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if value< 0:
            raise ValueError("value must be greater than 0")
        elif not isinstance(value, int):
            raise TypeError("value must be an integer")
        self.__size = value

    @property
    def position(self):
        return self.__positon

    @position.setter
    def position(self, value):
        if len(position) < 2 or not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in range(2):
            if self.__position[i] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
        [print("_") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print("_", end="") for i in range(self.__position[0])]
            [print("#",end="") for i in range(self.__size)]
            print("")
