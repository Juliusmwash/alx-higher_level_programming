#!/usr/bin/python3
""" Adds all arguments to a Python list, and then save them to a file """
import json
import sys
import os

save_file = __import__('5-save_to_json_file').save_to_json_file
load_file = __import__('6-load_from_json_file').load_from_json_file

check = 0
argv_list = []
if os.path.exists("add_item.json"):
    argv_list2 = load_file("add_item.json")
    for item in argv_list2:
        argv_list.append(item)
for item in sys.argv:
    if check:
        argv_list.append(item)
    else:
        check = 1
save_file(argv_list, "add_item.json")
