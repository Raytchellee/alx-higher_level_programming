#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    new_list = list(my_set)
    total = 0
    for idy in new_list:
        total += idy
    return total
