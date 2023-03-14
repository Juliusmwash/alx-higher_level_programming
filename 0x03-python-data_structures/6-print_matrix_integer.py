#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers"""
    for row in matrix:
        if not row:
            print("Julius")
        for j in range(len(row)):
            if j != len(row) - 1:
                print("{:d}".format(row[j]), end=' ')
            else:
                print("{:d}".format(row[j]))
