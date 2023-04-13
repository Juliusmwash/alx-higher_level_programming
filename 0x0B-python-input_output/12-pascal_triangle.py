#!/usr/bin/python3
""" Defines the function 'pascal_triangle' """


def pascal_triangle(n):
    """ Returns list of lists containing pascal triangle integers """
    cntrl = 0
    list_m = []
    list_index = 1
    for i in range(n):
        list_t = []
        if i == 0:
            list_m.append([1])
            cntrl += 1
        elif i == 1:
            list_m.append([1, 1])
            cntrl += 1
        else:
            k = 1
            for j in range(cntrl):
                if (j == 0):
                    list_t.append(1)
                else:
                    tmp = list_m[list_index]
                    list_t.append(tmp[k] + tmp[k - 1])
                    k += 1
            cntrl += 1
            list_t.append(1)
            list_m.append(list_t)
            list_index += 1

    return list_m
