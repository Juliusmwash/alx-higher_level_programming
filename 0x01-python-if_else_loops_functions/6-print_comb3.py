#!/usr/bin/python3
for i in range(0, 100):
    if i == 99:
        print("\n", end='')
    elif i // 10 == i % 10:
        continue
    elif ((i % 10) * 10 + (i // 10)) < i:
        continue
    elif i == 1:
        print("{:02d}".format(i), end='')
    else:
        print(", {:02d}".format(i), end='')
