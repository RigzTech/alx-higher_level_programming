#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = matrix[:]
    for i in range(len(new)):
        new[i] = list(map(lambda x: x ** 2, new[i]))
    return (new)
