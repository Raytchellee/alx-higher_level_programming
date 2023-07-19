#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    myList = list(a_dictionary.keys())
    myList.sort()
    for idx in myList:
        print("{}".format(idx))
