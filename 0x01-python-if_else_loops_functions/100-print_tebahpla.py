#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 != 0:
        num2 = i - 32
    else:
        num2 = i
    print("{:s}".format(chr(num2)), end='')
