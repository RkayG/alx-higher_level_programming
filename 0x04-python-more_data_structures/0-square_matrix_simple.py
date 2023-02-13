#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix is not None:
        square = []
        for row in matrix:
            square.append(list(map(lambda x: x**2, row)))
        return (square)
    return None
