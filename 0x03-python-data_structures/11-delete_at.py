#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if (idx < 0 or idx >= len(my_list)):
        return my_list
    new_list = []
    for idy in my_list:
        if (idy == idx ):
            continue
        else:
            new_list.append(idy)
    return new_list
