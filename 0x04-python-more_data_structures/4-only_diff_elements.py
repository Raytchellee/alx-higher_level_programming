#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    result = []
    for idy in set_1:
        if idy not in set_2:
            result.append(idy)
    for idy in set_2:
        if idy not in set_1:
            result.append(idy)
    return result
