#!/usr/bin/python3
"""Test Rectangle class."""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import sys
import io


class TestRectangleClass(unittest.TestCase):
    """Testing rectangle class."""

    def test_rect_1(self):
        """Normal test case."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 23)
        self.assertEqual(r2.id, 24)
        self.assertEqual(r3.id, 12)

    def test_rect_2_1(self):
        """Edge case missing arguments."""
        # r1 = Rectangle(1, 1, 1, 1, 9)
        with self.assertRaises(TypeError):
            Rectangle(1)

        with self.assertRaises(TypeError):
            Rectangle()

    def test_rect_2(self):
        """Magic method __str."""
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(str(r2), "[Rectangle] (25) 1/0 - 5/5")

    def test_rect_3(self):
        """Type errors."""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_rect_4(self):
        """Area method."""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_rect_5(self):
        """Display method."""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(4, 6)
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(
            capturedOutput.getvalue(),
            "####\n####\n####\n####\n####\n####\n"
        )
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r2 = Rectangle(2, 2)
        r2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(
            capturedOutput.getvalue(),
            "##\n##\n"
        )

    def test_rect_6(self):
        """Display2 method."""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(2, 3, 2, 2)
        r1.display()
        sys.stdout = sys.__stdout__
        s1 = """

  ##
  ##
  ##
"""
        self.assertEqual(capturedOutput.getvalue(), s1)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r2 = Rectangle(3, 2, 1, 0)
        r2.display()
        sys.stdout = sys.__stdout__
        s2 = """ ###
 ###
"""
        self.assertEqual(capturedOutput.getvalue(), s2)

    def test_rect_7(self):
        """Update method."""
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (34) 10/10 - 10/10")

        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")

        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")

        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_rect_8(self):
        """Update2 method."""
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (35) 10/10 - 10/10")

        r1.update(89, 3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 3/10")

        r1.update(1, 10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/1")

        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/10 - 1/1")

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")

    def test_rect_9(self):
        """To_dictionary method."""
        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(str(r1), "[Rectangle] (36) 1/9 - 10/2")

        r1_dictionary = r1.to_dictionary()
        self.assertEqual(
            r1_dictionary,
            {'x': 1, 'y': 9, 'id': 36, 'height': 2, 'width': 10}
        )

        self.assertTrue(type(r1_dictionary) is dict)

        r2 = Rectangle(1, 1)
        self.assertEqual(str(r2), "[Rectangle] (37) 0/0 - 1/1")

        r2.update(**r1_dictionary)
        self.assertEqual(str(r2), "[Rectangle] (36) 1/9 - 10/2")

        self.assertFalse(r1 == r2)
