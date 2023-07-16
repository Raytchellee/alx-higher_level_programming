#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        highest_val = my_list[0]
        for idx in my_list:
            if (idx > highest_val):
                highest_val = idx
    return highest_val
