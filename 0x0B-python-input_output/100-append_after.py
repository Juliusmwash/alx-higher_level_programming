#!/usr/bin/python3
""" Defines the function 'append_after' """


def append_after(filename="", search_string="", new_string=""):
    """ Appends new_string to the file if the search_string
    matches with a string in the filename file.
    new_string will be added immediately after
    the line containing the matched string. """

    with open(filename, mode="r", encoding="utf-8") as f:
        i = 0
        contents = f.readlines()
        for line in contents:
            if line.find(search_string) >= 0:
                contents.insert(i + 1, new_string)
            i += 1
    string = ""
    for line in contents:
        string += line
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(string)
