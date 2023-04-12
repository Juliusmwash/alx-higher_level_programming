#!/usr/bin/python3
""" Defines function 'write_file' """


def write_file(filename="", text=""):
    """ writes to a file and creates one if it doesn't exist """
    with open(filename, mode='w', encoding='utf-8') as w_file:
        w_file.write(text)
        return w_file.tell()

