#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    check_list = []
    for idx in my_list:
        if (idx % 2 == 0):
            check_list.append(True)
        else:
            check_list.append(False)
    return check_list
