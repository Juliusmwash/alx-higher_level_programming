#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1 = 0
    b1 = 0
    sum = 0
    sum2 = 0

    for i in range(2):
        if i:
            if len(tuple_a) == 0:
                a1 = 0
            elif len(tuple_a) < 2:
                a1 = 0
            else:
                a1 = tuple_a[i]
            if len(tuple_b) == 0:
                b1 = 0
            elif len(tuple_b) < 2:
                b1 = 0
            else:
                b1 = tuple_b[i]
            sum = a1 + b1

        else:
            if len(tuple_a) == 0:
                a1 = 0
            else:
                a1 = tuple_a[i]
            if len(tuple_b) == 0:
                b1 = 0
            else:
                b1 = tuple_b[i]
            sum2 = a1 + b1

    new_tuple = (sum2, sum) 
    return (new_tuple)
