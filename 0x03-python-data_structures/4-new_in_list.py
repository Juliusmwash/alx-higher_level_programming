#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a = []
    for item in my_list:
        a.append(item)
    if idx < 0:
        return a
    elif idx > len(a) - 1:
        return a
    else:
        for i in range(0, len(a)):
            if i == idx:
                a[i] = element
        return a
