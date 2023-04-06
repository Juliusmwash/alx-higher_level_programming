#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ class for performing tests on function 'max_integer' """
    def test_None(self):
        """
        function for checking the return value for
        an empty list given as an argument
        """
        result = max_integer([])
        self.assertEqual(result, None)

    def test_non_empty_list(self):
        """ 
        Function for checking the return value for
        non empty list given as an argument
        """
        result = max_integer([1, 2, 4, 3])
        self.assertEqual(result, 4)

    def test_no_argument(self):
        """
        Function for checking the error when no
        argument is provided as an argument
        """
        try:
            max_integer()
        except TypeError:
            self.assertRaises(TypeError)
