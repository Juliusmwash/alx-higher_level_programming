#!/usr/bin/python3
def no_c(my_string):
    str = ""
    for character in my_string:
        if character != 'c' and character != 'C':
            str += character
    return str
