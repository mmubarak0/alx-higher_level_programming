#!/usr/bin/python3
"""Base package."""

import json


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
