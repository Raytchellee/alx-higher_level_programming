#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if (a < b):
        c = add(a, b)
        for idx in range(4, 6):
            c = add(c, idx)
        return c
    else:
        c = sub(a, b)
        return c