#!/usr/bin/python3
""" Defines class 'Base' """
import json


class Base:
    """ The base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of
        list_dictionaries """
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        filename = cls.__name__ + '.json'
        if list_objs is not None:
            new_list = [obj.to_dictionary() for obj in list_objs]
            new_string = cls.to_json_string(new_list)
            with open(filename, mode='w', encoding='utf-8') as f:
                f.write(new_string)
        else:
            with open(filename, mode='w', encoding='utf-8') as f:
                f.write("[]")

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """  returns an instance with all attributes already set """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        filename = cls.__name__ + '.json'
        try:
            obj_list = []
            with open(filename, mode='r') as f:
                json_list = cls.from_json_string(f.read())
                for item in json_list:
                    obj = cls.create(**item)
                    obj_list.append(obj)
                return obj_list
        except FileNotFoundError:
            return []
