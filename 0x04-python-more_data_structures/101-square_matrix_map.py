#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda fun: list(map(lambda x: x*x, fun)), matrix)))
