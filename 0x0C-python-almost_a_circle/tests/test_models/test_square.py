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

    def test_1square(self):
        """ Second test case """
        s1 = Square(2, 2, 0, 85)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(s1)
            output = "[Square] (85) 2/0 - 2\n"
            self.assertEqual(fake_output.getvalue(), output)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(s1.area())
            output = "4\n"
            self.assertEqual(fake_output.getvalue(), output)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            s1.display()
            output = "  ##\n  ##\n"
            self.assertEqual(fake_output.getvalue(), output)

    def test_2square(self):
        """ Third test case """
        s1 = Square(3, 1, 3, 71)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(s1)
            output = "[Square] (71) 1/3 - 3\n"
            self.assertEqual(fake_output.getvalue(), output)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(s1.area())
            output = "9\n"
            self.assertEqual(fake_output.getvalue(), output)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            s1.display()
            output = "\n\n\n ###\n ###\n ###\n"
            self.assertEqual(fake_output.getvalue(), output)
