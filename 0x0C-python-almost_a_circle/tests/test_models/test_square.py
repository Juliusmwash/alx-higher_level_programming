#!/usr/bin/python3
""" module for square.py testing """
import unittest
from unittest.mock import patch
from io import StringIO
from models.square import Square

class Square_testing(unittest.TestCase):
    """ Test cases """
    def test_0square(self):
        """ First test case """
        s1 = Square(5, 0, 0, 43)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(s1)
            output = "[Square] (43) 0/0 - 5\n"
            self.assertEqual(fake_output.getvalue(), output)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(s1.area())
            output = "25\n"
            self.assertEqual(fake_output.getvalue(), output)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            s1.display()
            output = "#####\n#####\n#####\n#####\n#####\n"
            self.assertEqual(fake_output.getvalue(), output)
    """
    s1 = Square(5)
    print(s1)
    print(s1.area())
    s1.display()

    print("---")

    s2 = Square(2, 2)
    print(s2)
    print(s2.area())
    s2.display()

    print("---")

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display() """
