#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat = matrix.copy()

    def pow(x):
        return x**2
    for i in range(len(mat)):
        mat[i] = list(map(pow, matrix[i]))
    return mat
