#!/usr/bin/python3
"""Unittests for max_integer function
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer"""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([10, 5, 3]), 10)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-10, -5, -2]), -2)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-10, 5, -20, 7]), 7)

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_none_argument(self):
        """Ensure TypeError if None passed"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_no_argument(self):
        """Default empty list → returns None"""
        self.assertIsNone(max_integer())

    def test_string_list(self):
        """Compare characters (max lexicographically)"""
        self.assertEqual(max_integer("hello"), "o")

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.2, 3.7, 2.5]), 3.7)


if __name__ == '__main__':
    unittest.main()
