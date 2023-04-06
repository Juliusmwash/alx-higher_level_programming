#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ class for performing tests on function 'max_integer' """
    def test_no1(self):
        """
        function for checking the return value for
        an empty list given as an argument
        """
        result = max_integer([])
        self.assertEqual(result, None)

    def test_no2(self):
        """ 
        Function for checking the return value for
        non empty list given as an argument
        """
        result = max_integer([1, 2, 4, 3])
        self.assertEqual(result, 4)

    def test_no3(self):
        """
        Function for checking the error when no
        argument is provided as an argument
        """
        try:
            max_integer()
        except TypeError:
            self.assertRaises(TypeError)

    def test_no4(self):
        result = max_integer([1])
        self.assertEqual(result, 1)

    def test_no5(self):
        result = max_integer([4, 2, 3, 1])
        self.assertEqual(result, 4)

    def test_no6(self):
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_no7(self):
        result = max_integer([3, -9, 2, 4])
        self.assertEqual(result, 4)

    def test_no8(self):
        result = max_integer([-1, -2, -3, -4])
        self.assertEqual(result, -1)
