#!/usr/bin/python3
import json

a = [[1, 2, 3], [4, 5, 6]]
b = [json.dumps(obj) for obj in a]
c = json.dumps(b)
d = None
e = [json.dumps(obj) for obj in d]
print("e")
print(e)
print(type(e))
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
print("a")
for i in a:
    print(type(i))
print("b")
for i in b:
    print(type(i))
print("c")
for i in c:
    print(type(i))
