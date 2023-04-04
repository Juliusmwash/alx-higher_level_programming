#!/usr/bin/python3
""" Making a rectangle class """


class Rectangle:
    """ An empty rectangle class """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ object initializer

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Function for getting the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width value """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ gets the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height of the rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of the rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ returns the perimeter of the rectangle """
        if self.__width == 0:
            return 0
        elif self.__height == 0:
            return 0
        return (self.__width * 2 + self.__height * 2)

    def __str__(self):
        """ print the rectangle with the character # """
        if self.__width == 0 or self.__height == 0:
            return ""
        if isinstance(self.print_symbol, str):
            a = ""
            for j in range(self.__height):
                for i in range(self.__width):
                    a += self.print_symbol
                    if j != self.__height - 1 and i == self.__width - 1:
                        a += "\n"
            return a
        else:
            a = ""
            for j in range(self.__height):
                for i in range(self.__width):
                    a += str(self.print_symbol)
                    if j != self.__height - 1 and i == self.__width - 1:
                        a += "\n"
            return a

    def __repr__(self):
        """ return a string representation of the rectangle """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ prints a message when an object is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
