#!/usr/bin/python3
def uppercase(str):
    for idx in range(len(str)):
        c = str[idx]
        if (ord(c) in range(97, 123)):
            c = chr(ord(c) - 32)
        if (idx == len(str) - 1):
            print(c)
        else:
            print(c, end='')
