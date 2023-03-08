#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = ""
    i = 0
    for c in str:
        if i != n:
            str2 += c
        i += 1
    return str2

print(remove_char_at("Best School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))
