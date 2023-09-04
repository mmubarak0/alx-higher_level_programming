#!/usr/bin/python3
"""Unittest for max_integer([..])."""

import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Test max integer function."""

    def test_simple_list(self):
        """Simple test."""
        li = [1, 2, 3, 4]
        self.assertEqual(max_integer(li), 4)

    def test_simple_list_2(self):
        """Simple test 2."""
        li = [1, -2, 4, 3]
        self.assertEqual(max_integer(li), 4)

    def test_simple_list_3(self):
        """Simple test 3."""
        li = [1]
        self.assertEqual(max_integer(li), 1)

    def test_simple_list_4(self):
        """Simple test 4."""
        li = [1, 1.5]
        self.assertEqual(max_integer(li), 1.5)

    # def test_invalid_list(self):
    #     """Invalid list test."""
    #     li = "1245"
    #     with self.assertRaises(TypeError):
    #         result = max_integer(li)

    def test_invalid_list_item(self):
        """Invalid list item test."""
        li = ["1", 2, "2"]
        with self.assertRaises(TypeError):
            result = max_integer(li)

    def test_empty_list(self):
        """Empty list test."""
        li = []
        self.assertEqual(max_integer(li), None)
