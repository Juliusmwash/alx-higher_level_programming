#!/usr/bin/python3
def max_integer(my_list=[]):
    max_int = None
    count = 0

    if my_list:
        for i in my_list:
            if count == 0:
                max_int = i
                count += 1
            elif i > max_int:
                max_int = i
        return max_int
