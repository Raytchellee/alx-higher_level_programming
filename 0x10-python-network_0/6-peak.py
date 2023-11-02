#!/usr/bin/python3
""" returns higest num in array """


def find_peak(list_of_integers):
    """ returns higest num """
    highest = None
    if len(list_of_integers) == 0:
        return None
    list_of_integers.sort(reverse=True)
    return list_of_integers[0]
