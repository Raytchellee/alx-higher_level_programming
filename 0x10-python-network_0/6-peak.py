#!/usr/bin/python3
""" returns higest num in array """


def find_peak(list_of_integers):
    """ returns higest num """
    highest = None
    if type(list_of_integers) != list:
        return
    if len(list_of_integers) == 0:
        return None
    return max(list_of_integers)
