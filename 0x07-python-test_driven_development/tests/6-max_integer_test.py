#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class for unittesting max_integer([..])"""

    def test_module(self):
        """Test the module docstring"""
        test_case = __import__('6-max_integer').__doc__
        self.assertTrue(len(test_case) > 1)

    def test_function(self):
        """Test the function docstring"""
        test_case = max_integer.__doc__
        self.assertTrue(len(test_case) > 1)

    def test_list_ordered(self):
        """Test list in ordered form"""
        test_case = [16, 34, 54, 66, 67, 163]
        self.assertEqual(max_integer(test_case), 163)

    def test_list_unordered(self):
        """Test list in unordered form"""
        test_case = [34, 66, 54, 163, 67]
        self.assertEqual(max_integer(test_case), 163)

    def test_max_first(self):
        """Test list starting with maimum value"""
        test_case = [70, 34, 66, 54, 16]
        self.assertEqual(max_integer(test_case), 70)

    def test_empty(self):
        """Test empty list"""
        test_case = []
        self.assertEqual(max_integer(test_case), None)

    def test_single_list(self):
        """Test a single element list"""
        test_case = [99]
        self.assertEqual(max_integer(test_case), 99)

    def test_zero_args(self):
        """Tests for the function with no argument"""
        self.assertIsNone(max_integer())

    def test_none_arg(self):
        """Tests None as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_randomized_list(self):
        """Tests list containing random values"""
        test_case = [7, 8.5, 2, "Ray", "World", 9]
        with self.assertRaises(TypeError):
            max_integer(test_case)

    def test_floats_list(self):
        """Test a list of floats"""
        test_case = [12.5, 67.9, 44.9, 7.876, -10.2]
        self.assertEqual(max_integer(test_case), 67.9)

    def test_combined_values(self):
        """Test list of combined values"""
        test_case = [12.5, 67.9, 44, -2, 28]
        self.assertEqual(max_integer(test_case), 67.9)

    def test_negative(self):
        """Tests negative included list"""
        test_case = [450, 700, 36, -99, 78, 90]
        self.assertEqual(max_integer(test_case), 700)

    def test_negative_inputs(self):
        """Test for all negative inputs"""
        test_case = [-10, -40, -20, -3]
        self.assertEqual(max_integer(test_case), -3)

    def test_string(self):
        """Test for string input"""
        test_case = "Stringy"
        self.assertEqual(max_integer(test_case), 'y')

    def test_strings(self):
        """Test for list of strings"""
        test_case = ["Ray", "to", "your", "world"]
        self.assertEqual(max_integer(test_case), "your")

    def test_null_string(self):
        """Tests for empty string"""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
