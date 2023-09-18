#!/usr/bin/python3
"""Test base class."""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json


class TestBaseClass(unittest.TestCase):
    """Testing base class."""

    def test_1(self):
        """Test normal case."""
        a = Base()
        b = Base()
        c = Base()
        self.assertEqual(a.id, 1)
        self.assertEqual(b.id, 2)
        self.assertEqual(c.id, 3)

    def test_2(self):
        """Change id."""
        a = Base()
        b = Base()
        c = Base(15)
        d = Base()
        self.assertEqual(a.id, 4)
        self.assertEqual(b.id, 5)
        self.assertEqual(c.id, 15)
        self.assertEqual(d.id, 6)

    def test_3(self):
        """Change id."""
        a = Base()
        b = Base()
        c = Base(1)
        d = Base()
        e = Base(3)
        self.assertEqual(a.id, 7)
        self.assertEqual(b.id, 8)
        self.assertEqual(c.id, 1)
        self.assertEqual(d.id, 9)
        self.assertEqual(e.id, 3)

    def test_4(self):
        """Negative ids."""
        a = Base(-4)
        b = Base(-5)
        self.assertEqual(a.id, -4)
        self.assertEqual(b.id, -5)

    def test_5(self):
        """To_json_string method."""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(
            dictionary, {'x': 2, 'y': 8, 'id': 10, 'height': 7, 'width': 10})
        self.assertTrue(type(dictionary) is dict)
        self.assertEqual(
            json_dictionary,
            '[{"x": 2, "y": 8, "id": 10, "height": 7, "width": 10}]')
        self.assertTrue(type(json_dictionary) is str)

    def test_6(self):
        """Save_to_file method."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            a = [
                    {"x": 2, "y": 8, "id": 11, "height": 7, "width": 10},
                    {"x": 0, "y": 0, "id": 12, "height": 4, "width": 2}
                ]
            self.assertEqual(a, json.loads(file.read()))

    def test_7(self):
        """From_json_string method."""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertTrue(type(list_input) is list)
        self.assertEqual(
            list_input, [
                {'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}])
        self.assertTrue(type(json_list_input) is str)
        self.assertEqual(
            json.loads(json_list_input),
            [
                {"id": 89, "width": 10, "height": 4},
                {"id": 7, "width": 1, "height": 7}
            ]
        )
        self.assertTrue(type(list_output) is list)
        self.assertEqual(
            list_output,
            [
                {'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}
            ]
        )

    def test_8(self):
        """Create method."""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(f"{r1}", "[Rectangle] (13) 1/0 - 3/5")
        self.assertEqual(f"{r2}", "[Rectangle] (13) 1/0 - 3/5")
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_9(self):
        """Load_from_file method."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(
            f"{list_rectangles_input[0]}", "[Rectangle] (15) 2/8 - 10/7")
        self.assertEqual(
            f"{list_rectangles_input[1]}", "[Rectangle] (16) 0/0 - 2/4")
        self.assertEqual(
            f"{list_rectangles_output[0]}", "[Rectangle] (15) 2/8 - 10/7")
        self.assertEqual(
            f"{list_rectangles_output[1]}", "[Rectangle] (16) 0/0 - 2/4")
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(f"{list_squares_input[0]}", "[Square] (19) 0/0 - 5")
        self.assertEqual(f"{list_squares_input[1]}", "[Square] (20) 9/1 - 7")
        self.assertEqual(f"{list_squares_output[0]}", "[Square] (19) 0/0 - 5")
        self.assertEqual(f"{list_squares_output[1]}", "[Square] (20) 9/1 - 7")


if __name__ == '__main__':
    unittest.main()
