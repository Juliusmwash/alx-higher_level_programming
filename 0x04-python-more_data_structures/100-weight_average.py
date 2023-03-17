#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    avrg_sum = 0

    if len(my_list) == 0:
        return 0;
    for i in range(len(my_list)):
        mult = 1

        for j in range(len(my_list[i])):
            mult *= my_list[i][j]
            if j == len(my_list[i]) - 1:
                sum += mult
                avrg_sum += my_list[i][j]
    return sum / avrg_sum
