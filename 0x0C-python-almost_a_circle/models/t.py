#!/usr/bin/python3

class Testing:
    def __init__(self):
        self.id = 1
        self.__width = 2
        self.__height = 2
        self.__x = 2
        self.__y = 2

    def change_att(self, *args):
        length = len(args)
        for i in range(length):
            if i == 0 and args[i] != None:
                self.id = args[i]
            elif i == 1 and args[i] != None:
                self.__width = args[i]
            elif i == 2 and args[i] != None:
                self.__height = args[i]
            elif i == 3 and args[i] != None:
                self.__x = args[i]
            elif i == 4 and args[i] != None:
                self.__y = args[i]
    def print_data(self):
        print(self.id)
        print(self.__width)
        print(self.__height)
        print(self.__x)
        print(self.__y)

a = Testing()
a.change_att(5, 6, 7, 8, 9)
a.change_att(10, 11)
a.change_att(None, None, None, None, 98)
a.change_att()
a.print_data()
