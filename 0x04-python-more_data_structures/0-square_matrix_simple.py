#!/usr/bin/python3

def pow(x):
    return x**2
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for i in range(len(matrix)):
        new_matrix[i] = list(map(pow, matrix[i]))

    return (new_matrix)
