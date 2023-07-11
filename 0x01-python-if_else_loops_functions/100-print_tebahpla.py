#!/usr/bin/python3
def print_rev_alph():
    for idx in range(ord('Z'), ord('A') - 1, -1):
        if (idx % 2 == 0):
            char = chr(idx + 32)
        else:
            char = chr(idx)
        print("{}".format(char), end='')


print_rev_alph()
