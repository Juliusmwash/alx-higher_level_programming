#!/usr/bin/python3
"""
Define function "text_indentation".
This function prints a text with 2 new lines
after each of these characters: ., ? and :.
"""


def text_indentation(text):
    """ prints text with indentation """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    check = 0
    for i in range(len(text)):
        char = text[i]
        if check and char == ' ':
            print("", end="")
        elif check and char != ' ':
            check = 0
            print("{:s}".format(char), end="")
        elif char == '.' or char == ':' or char == '?':
            print("{:s}\n".format(char))
            check = 1
        else:
            print("{:s}".format(char), end='')
