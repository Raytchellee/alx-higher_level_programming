#!/usr/bin/python3
def weight_average(my_list=[]):
    if (len(my_list) == 0):
        return 0
    sum = 0
    div = 0
    for idx in my_list:
        sum += idx[0] * idx[1]
        div += idx[1]
    return sum/div
