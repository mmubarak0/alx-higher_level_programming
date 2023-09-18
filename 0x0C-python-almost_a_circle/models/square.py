#!/usr/bin/python3
"""Square package."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Square init method."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Magic string."""
        return f"[Square] ({self.id}) \
{self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Square size getter."""
        return self.width

    @size.setter
    def size(self, size):
        """Square size setter."""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update method."""
        for name in kwargs.keys():
            if name == 'id':
                self.validate(name, kwargs[name], 'int')
                self.id = kwargs[name]
            if name == 'size':
                self.validate(name, kwargs[name], 'int', 'pos+', 'inf')
                self.width = kwargs[name]
                self.height = kwargs[name]
            if name in ['x', 'y']:
                self.validate(name, kwargs[name], 'int', 'pos', 'inf')
                self.x = kwargs['x'] if 'x' in kwargs else self.x
                self.y = kwargs['y'] if 'y' in kwargs else self.y

        for idx, value in enumerate(args):
            if idx == 0:
                self.validate('id', value, 'int')
                self.id = value
            elif idx == 1:
                self.validate('size', value, 'int', 'pos+', 'inf')
                self.width = value
                self.height = value
            elif idx == 2:
                self.validate('x', value, 'int', 'pos', 'inf')
                self.x = value
            elif idx == 3:
                self.validate('y', value, 'int', 'pos', 'inf')
                self.y = value

    def to_dictionary(self):
        """Return dict repr."""
        result = {
            'id': self.id, 'x': self.x,
            'size': self.width, 'y': self.y,
            }
        return result
