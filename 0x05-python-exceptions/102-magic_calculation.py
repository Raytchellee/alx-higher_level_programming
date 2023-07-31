#!/usr/bin/python3
def magic_calculation(a, b):
    total = 0

    for idx in range(1, 3):
        try:
            if (idx > a):
                raise Exception("Too far")
            total += (a ** b) / idx
        except:
            total = a + b
            break
    return total
