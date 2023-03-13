#!/usr/bin/python3
def element_at(my_list, idx):
    if idx > len(my_list) - 1:
        return None
    elif idx < 0:
        return None
    else:
        j = len(my_list)
        for i in range(0, len(my_list)):
            if (i == idx):
                return my_list[i]
