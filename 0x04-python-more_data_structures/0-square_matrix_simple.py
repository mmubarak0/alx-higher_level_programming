#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if type(matrix) is list:
        sqr_matrix = [[j**2 for j in i] for i in matrix]
        return sqr_matrix
