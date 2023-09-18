#!/usr/bin/python3
"""Test Square class."""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import sys
import io


class TestSquareClass(unittest.TestCase):
    """Testing square class."""

    def test_square_1(self):
        """Normal test."""
        s1 = Square(5)
        self.assertEqual(
            str(s1),
            "[Square] (38) 0/0 - 5"
        )

        self.assertEqual(s1.area(), 25)

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        s1.display()
        sys.stdout = sys.__stdout__
        dx1 = """#####
#####
#####
#####
#####
"""
        self.assertEqual(capturedOutput.getvalue(), dx1)

        s2 = Square(2, 2)
        self.assertEqual(
            str(s2),
            "[Square] (39) 2/0 - 2"
        )

        self.assertEqual(s2.area(), 4)

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        s2.display()
        sys.stdout = sys.__stdout__
        dx2 = """  ##
  ##
"""
        self.assertEqual(capturedOutput.getvalue(), dx2)

        s3 = Square(3, 1, 3)
        self.assertEqual(
            str(s3),
            "[Square] (40) 1/3 - 3"
        )

        self.assertEqual(s3.area(), 9)

        dx3 = """


 ###
 ###
 ###
"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        s3.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), dx3)

    def test_square_2(self):
        """Size test."""
        s1 = Square(5)
        self.assertEqual(
            str(s1),
            "[Square] (41) 0/0 - 5"
        )

        self.assertEqual(s1.size, 5)

        s1.size = 10
        self.assertEqual(
            str(s1),
            "[Square] (41) 0/0 - 10"
        )

        with self.assertRaises(TypeError):
            s1.size = "9"

    def test_square_3(self):
        """Update method."""
        s1 = Square(5)
        self.assertEqual(
            str(s1),
            "[Square] (42) 0/0 - 5"
        )

        s1.update(10)
        self.assertEqual(
            str(s1),
            "[Square] (10) 0/0 - 5"
        )

        s1.update(1, 2)
        self.assertEqual(
            str(s1),
            "[Square] (1) 0/0 - 2"
        )

        s1.update(1, 2, 3)
        self.assertEqual(
            str(s1),
            "[Square] (1) 3/0 - 2"
        )

        s1.update(1, 2, 3, 4)
        self.assertEqual(
            str(s1),
            "[Square] (1) 3/4 - 2"
        )

        s1.update(x=12)
        self.assertEqual(
            str(s1),
            "[Square] (1) 12/4 - 2"
        )

        s1.update(size=7, y=1)
        self.assertEqual(
            str(s1),
            "[Square] (1) 12/1 - 7"
        )

        s1.update(size=7, id=89, y=1)
        self.assertEqual(
            str(s1),
            "[Square] (89) 12/1 - 7"
        )

    def test_square_4(self):
        """To_dictionary method."""
        s1 = Square(10, 2, 1)
        self.assertEqual(
            str(s1),
            "[Square] (43) 2/1 - 10"
        )

        s1_dictionary = s1.to_dictionary()
        self.assertEqual(
            s1_dictionary,
            {'id': 43, 'x': 2, 'size': 10, 'y': 1}
        )

        self.assertTrue(type(s1_dictionary) is dict)

        s2 = Square(1, 1)
        self.assertEqual(
            str(s2),
            "[Square] (44) 1/0 - 1"
        )

        s2.update(**s1_dictionary)
        self.assertEqual(
            str(s2),
            "[Square] (43) 2/1 - 10"
        )

        self.assertFalse(s1 == s2)
