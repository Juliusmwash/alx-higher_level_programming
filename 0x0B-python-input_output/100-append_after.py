#!/usr/bin/python3
""" Defines the function 'append_after' """


def append_after(filename="", search_string="", new_string=""):
    """ Appends new_string to the file if the search_string
    matches with a string in the filename file.
    new_string will be added immediately after
    the line containing the matched string. """

    string = ""
    with open(filename, mode="r", encoding="utf-8") as f:
        for line in f:
            string += line
            if search_string in line:
                string += new_string
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(string)
