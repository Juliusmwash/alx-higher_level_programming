#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    if my_list:
        for item in my_list:
            if not item % 2:
                new_list.append(True)
            else:
                new_list.append(False)
        return new_list
