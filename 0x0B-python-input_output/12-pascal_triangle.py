#!/usr/bin/python3
"""Technical interview assessment"""


def pascal_triangle(n):
    """Returns pascal triangle"""
    result = []
    if n <= 0:
        return result

    result.append([1])

    for idx in range(1, n):
        string = result[idx - 1]
        temp = []
        for idy in range(len(string)):
            if idy == 0:
                temp.append(string[idy])
            if idy != len(string) - 1 and idy + 1 < len(string):
                s = str(int(string[idy]) + int(string[idy + 1]))
                temp.append(s)
            if idy is len(string) - 1:
                temp.append(string[idy])
        result.append(temp)

    return result
