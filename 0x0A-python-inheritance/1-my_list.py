#!/usr/bin/python3
""" Defines class 'MyList' that inherits from 'list' """


class list:
    """ contains a list object attribute """
    def __init__(self):
        """ class constructor """
        self.my_list = []

    def append(self, value):
        """ adds item to the list """
        self.my_list.append(value)


class MyList(list):
    """ inherits from class 'List' """
    def print_sorted(self):
        """ prints sorted list """
        print(sorted(self.my_list))

    def __str__(self):
        """ prints a non-sorted list """
        return str(self.my_list)
