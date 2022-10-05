#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_mat = matrix.copy()
    for row in range(len(matrix)):
        new_mat[row] = list(map(lambda x: x**2, new_mat[row]))
    return new_mat

