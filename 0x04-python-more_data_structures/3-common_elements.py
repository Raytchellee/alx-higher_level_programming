#!/usr/bin/python3
def common_elements(set_1, set_2):
    result = []
    for idy in set_1:
        if idy in set_2:
            result.append(idy)
    return result
