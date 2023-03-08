#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        num2 = (number * -1) % 10
    else:
        num2 = number % 10
    print("{:d}".format(num2), end='')
    return num2
