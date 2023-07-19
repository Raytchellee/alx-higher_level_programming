#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for idx in matrix:
        temp = []
        for idy in idx:
            temp.append(idy * idy)
        result.append(temp)

    return result
