#!/usr/bin/python3
""" Defines class 'Base' """
import json
import csv
import time


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
                    obj_list.append(cls.create(**item))
                return obj_list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serializes object files """
        name = cls.__name__ + '.csv'
        list_dicts = []
        for obj in list_objs:
            list_dicts.append(obj.to_dictionary())
        if cls.__name__ == 'Rectangle':
            fd_names = ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == 'Square':
            fd_names = ['id', 'size', 'x', 'y']

        with open(name, mode='w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fd_names)
            writer.writeheader()
            for row in list_dicts:
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """ deserializes object files """
        name = cls.__name__ + '.csv'
        list_objs = []
        list_dicts = []
        try:
            with open(name, mode='r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    row['id'] = int(row['id'])
                    row['x'] = int(row['x'])
                    row['y'] = int(row['y'])
                    if cls.__name__ == 'Rectangle':
                        row['width'] = int(row['width'])
                        row['height'] = int(row['height'])
                    elif cls.__name__ == 'Square':
                        row['size'] = int(row['size'])
                    list_dicts.append(row)

                for dictionary in list_dicts:
                    obj = cls.create(**dictionary)
                    list_objs.append(obj)
                return list_objs
        except FileNotFoundError:
            return []

    def draw(list_rectangles, list_squares):
        """
        Draws the given rectangle and square objects.
        Please import time, to enjoy the scene.
        """
        window = turtle.Screen()
        turtle.speed(5)
        turtle.pensize(2)
        turtle.hideturtle()
        turtle.penup()
        turtle.bgcolor("pink")
        colours = ["blue", "green", "red"]
        k = 0
        for obj in list_rectangles:
            turtle.color(colours[k])
            turtle.begin_fill()
            turtle.goto(obj.x, obj.y)
            turtle.pendown()
            for i in range(2):
                turtle.forward(obj.width)
                turtle.left(90)
                turtle.forward(obj.height)
                turtle.left(90)
            k += 1
            turtle.end_fill()
            turtle.penup()
            time.sleep(3)
            turtle.clear()
        k = 0
        colours = ["orange", "purple", "yellow"]
        for obj in list_squares:
            turtle.color(colours[k])
            turtle.begin_fill()
            turtle.goto(obj.x, obj.y)
            turtle.pendown()
            for i in range(4):
                turtle.forward(obj.size)
                turtle.left(90)
                k += 1
            turtle.end_fill()
            turtle.penup()
            time.sleep(3)
            turtle.clear()
