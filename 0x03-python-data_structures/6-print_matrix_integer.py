#!/usr/bin/python3
for idx in range(len(matrix)):
    for idy in range(len(matrix[idx])):
        if (idy == len(matrix[idx]) - 1):
            print("{:d}".format(matrix[idx][idy]))
        else:
            print("{:d}".format(matrix[idx][idy]), end=" ")
