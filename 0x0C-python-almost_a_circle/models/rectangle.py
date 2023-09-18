#!/usr/bin/python3
"""Rectangle package."""

from models.base import Base


class Rectangle(Base):
    """Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init the Rectangle instance."""
        self.validate('width', width, 'int', 'pos+', 'inf')
        self.__width = width
        self.validate('height', height, 'int', 'pos+', 'inf')
        self.__height = height
        self.validate('x', x, 'int', 'pos', 'inf')
        self.__x = x
        self.validate('y', y, 'int', 'pos', 'inf')
        self.__y = y
        self.print_character = '#'
        super().__init__(id)

    @property
    def width(self):
        """Width getter."""
        return self.__width

    @property
    def height(self):
        """Height getter."""
        return self.__height

    @property
    def x(self):
        """X getter."""
        return self.__x

    @property
    def y(self):
        """Y getter."""
        return self.__y

    @width.setter
    def width(self, width):
        self.validate('width', width, 'int', 'pos+', 'inf')
        self.__width = width

    @height.setter
    def height(self, height):
        self.validate('height', height, 'int', 'pos+', 'inf')
        self.__height = height

    @x.setter
    def x(self, x):
        self.validate('x', x, 'int', 'pos', 'inf')
        self.__x = x

    @y.setter
    def y(self, y):
        self.validate('y', y, 'int', 'pos', 'inf')
        self.__y = y

    def area(self):
        """Return the area of rectangle."""
        return self.__width * self.__height

    def display(self):
        """Display the rectangle."""
        pc = self.print_character
        disp = []
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            disp.append([" " for i in range(self.__x)])
            for j in range(self.__width):
                disp[i].append(pc)
            disp[i] = "".join(disp[i])
        disp = "\n".join(disp)
        print(disp)

    def __str__(self):
        """Magic string."""
        return f"[Rectangle] ({self.id}) \
{self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Update method."""
        for name in kwargs.keys():
            if name == 'id':
                self.validate(name, kwargs[name], 'int')
                self.id = kwargs[name]
            if name in ['width', 'height']:
                self.validate(name, kwargs[name], 'int', 'pos+', 'inf')
                self.__width = kwargs['width'] \
                    if 'width' in kwargs else self.__width
                self.__height = kwargs['height'] \
                    if 'height' in kwargs else self.__height
            if name in ['x', 'y']:
                self.validate(name, kwargs[name], 'int', 'pos', 'inf')
                self.__x = kwargs['x'] if 'x' in kwargs else self.__x
                self.__y = kwargs['y'] if 'y' in kwargs else self.__y

        for idx, value in enumerate(args):
            if idx == 0:
                self.validate('id', value, 'int')
                self.id = value
            elif idx == 1:
                self.validate('width', value, 'int', 'pos+', 'inf')
                self.__width = value
            elif idx == 2:
                self.validate('height', value, 'int', 'pos+', 'inf')
                self.__height = value
            elif idx == 3:
                self.validate('x', value, 'int', 'pos', 'inf')
                self.__x = value
            elif idx == 4:
                self.validate('y', value, 'int', 'pos', 'inf')
                self.__y = value

    def to_dictionary(self):
        """Return dict repr."""
        result = {
            'x': self.__x, 'y': self.__y,
            'id': self.id, 'height': self.__height,
            'width': self.__width,
            }
        return result
