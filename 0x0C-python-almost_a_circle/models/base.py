#!/usr/bin/python3
"""Base package."""

import json
import csv
import turtle


class Base:
    """Base class."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Init the base instance."""
        if id is not None:
            self.validate('id', id, 'int')
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def validate(self, name, obj, *args):
        """Validate an object."""
        if 'int|float' in args:
            if type(obj) is not int and type(obj) is not float:
                raise TypeError(f'{name} must be an integer or float')
        if 'int' in args:
            if type(obj) is not int:
                raise TypeError(f'{name} must be an integer')
        if 'float' in args:
            if type(obj) is not float:
                raise TypeError(f'{name} must be a float')
        if 'str' in args:
            if type(obj) is not str:
                raise TypeError(f'{name} must be a string')
        if 'pos' in args:
            if obj < 0:
                raise ValueError(f'{name} must be >= 0')
        if 'pos+' in args:
            if obj <= 0:
                raise ValueError(f'{name} must be > 0')
        if 'inf' in args:
            if obj == float('inf') or obj == -float('inf'):
                raise OverflowError(f'{name} overflow error')

    @staticmethod
    def to_json_string(list_dictionaries):
        """List to Json."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Object to json file."""
        with open(f"{cls.__name__}.json", 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dict = [ob.to_dictionary() for ob in list_objs]
                res = cls.to_json_string(list_dict)
                f.write(res)

    @staticmethod
    def from_json_string(json_string):
        """From json string."""
        if json_string is None or len(json.loads(json_string)) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Dect to instance."""
        if cls.__name__ == 'Rectangle':
            new_rect = cls(1, 1)
            new_rect.update(**dictionary)
        else:
            new_rect = cls(1)
            new_rect.update(**dictionary)
        return new_rect

    @classmethod
    def load_from_file(cls):
        """Load json from a file."""
        res = []
        try:
            with open(f"{cls.__name__}.json", encoding='utf-8') as f:
                obj = cls.from_json_string(f.read().rstrip())
                for o in obj:
                    new_instance = cls.create(**o)
                    res.append(new_instance)
        except FileNotFoundError:
            return res
        return res

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Docs here."""
        with open(f"{cls.__name__}.csv", "w", encoding='utf-8') as f:
            list_dicts = [ob.to_dictionary() for ob in list_objs]
            if cls.__name__ == 'Rectangle':
                fields = ['id', 'width', 'height', 'x', 'y']
            else:
                fields = ['id', 'size', 'x', 'y']
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            for obj in list_dicts:
                writer.writerow(obj)

    @classmethod
    def load_from_file_csv(cls):
        """Docs here."""
        with open(f"{cls.__name__}.csv", "r", encoding='utf-8') as f:
            dictreader = csv.DictReader(f)
            res = []
            for obj in dictreader:
                res_dict = {}
                if cls.__name__ == 'Rectangle':
                    res_dict['id'] = int(obj['id'])
                    res_dict['width'] = int(obj['width'])
                    res_dict['height'] = int(obj['height'])
                    res_dict['x'] = int(obj['x'])
                    res_dict['y'] = int(obj['y'])
                else:
                    res_dict['id'] = int(obj['id'])
                    res_dict['size'] = int(obj['size'])
                    res_dict['x'] = int(obj['x'])
                    res_dict['y'] = int(obj['y'])
                new_instance = cls.create(**res_dict)
                res.append(new_instance)
            return res
        return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Docs here."""
        PEN_COLORS = ["purple", "red", "green", "orange", "blue", "yellow"]
        wn = turtle.Screen()
        s = turtle.Turtle()
        for rect in list_rectangles:
            s.color(PEN_COLORS[rect.id % 6])
            s.fillcolor(PEN_COLORS[rect.id % 6])
            s.penup()
            s.speed(5)
            s.setx(rect.x)
            s.sety(rect.y)
            s.pendown()
            s.speed(1)
            if rect.id % 2:
                s.begin_fill()
            s.forward(rect.width)
            s.right(90)
            s.forward(rect.height)
            s.right(90)
            s.forward(rect.width)
            s.right(90)
            s.forward(rect.height)
            s.end_fill()
        for square in list_squares:
            s.color(PEN_COLORS[square.id % 6])
            s.fillcolor(PEN_COLORS[square.id % 6])
            s.penup()
            s.speed(5)
            s.setx(square.x)
            s.sety(square.y)
            s.pendown()
            s.speed(1)
            if square.id % 2:
                s.begin_fill()
            s.forward(square.size)
            s.right(90)
            s.forward(square.size)
            s.right(90)
            s.forward(square.size)
            s.right(90)
            s.forward(square.size)
            s.end_fill()
        turtle.done()
