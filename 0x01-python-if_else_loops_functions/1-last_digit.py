#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number2 = number % 10
if number < 0:
    number2 *= -1
if number2 > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, number2))
elif number2 == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, number2))
elif number2 < 6:
    print("Last digit of {:d} is {:d} and is less than 5 and not 0".format(number, number2))

