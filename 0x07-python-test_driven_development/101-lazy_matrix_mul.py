#!/usr/bin/python3
""" Defines the function ''matrix_mul''
This function multiplies two matrixes
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Function for multiplying two matrixes """
    c = np.dot(m_a, m_b)
    return c
