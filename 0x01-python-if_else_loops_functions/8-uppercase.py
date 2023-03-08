#!/usr/bin/python3
def uppercase(str):
    newStr = ""
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            number = ord(c) - 32
            letter = chr(number)
            newStr += letter
        else:
            newStr += c
    print("{:s}".format(newStr))
