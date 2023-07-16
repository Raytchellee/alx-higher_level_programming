#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print("", end="")
    else:
        for idx in range(len(matrix)):
            for idy in range(len(matrix[idx])):
                if (idy != len(matrix[idx]) - 1):
                    print("{:d} ".format(matrix[idx][idy]), end='')
                else:
                    print("{:d}".format(matrix[idx][idy]))
