#!/usr/bin/python3
def search_replace(my_list, search, replace):
    result = []
    for idy in my_list:
        if (idy == search):
            result.append(replace)
        else:
            result.append(idy)
    return result
