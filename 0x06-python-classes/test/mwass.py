#!/usr/bin/python3
def mwass(size):
    if size < 0:
        raise TypeError("unknown error")
    try:
        if size > 0:
            print("not zero")
    except ValueError:
        print("zero not allowed")
    else:
        print("size not zero")
    finally:
        print("At the end")

mwass(-5)
