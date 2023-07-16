#!/usr/bin/python3
for idx in range(len(matrix)):
    for idy in range(len(matrix[idx])):
        print("{:d}".format(matrix[idx][idy]), end="")
        if (idy != len(matrix[idx]) - 1):
            print(" ", end="")
        print("")
