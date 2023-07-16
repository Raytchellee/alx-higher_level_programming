#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for idx in range(len(matrix)):
        for idy in range(len(matrix[idx])):
            if (idy != len(matrix[idx]) - 1):
                print("{} ".format(matrix[idx][idy]), end='')
            else:
                print("{}".format(matrix[idx][idy]))
