#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda x : list(map(lambda y: y**2, x)), matrix))
or
"""
    mat = matrix.copy()
    for i in matrix:
        mat.append( list(map(lambda x : x ** 2, i)))
    del mat[:len(matrix)]
    return mat
"""
