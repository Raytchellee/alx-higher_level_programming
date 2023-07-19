#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max = float('-inf')
        key_name = ""
        for key in a_dictionary:
            if (a_dictionary[key] > max):
                max = a_dictionary[key]
                key_name = key
        return key_name
