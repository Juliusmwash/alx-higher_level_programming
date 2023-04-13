#!/usr/bin/python3
""" Defines function 'class_to_json' """
import json


def class_to_json(obj):
    """ returns the dictionary description with simple
    data structure(list, dictionary, string, integer and boolean)
    for JSON serialization of an object """
    """class MyEncoder(json.JSONEncoder):
        #generates a dictionary
        def default(self, obj):
            #Convert objects to a dictionary of their
            #representation
            return obj.__dict__
    json_str = json.dumps(obj, cls=MyEncoder)
    return json_str"""
    return obj.__dict__
