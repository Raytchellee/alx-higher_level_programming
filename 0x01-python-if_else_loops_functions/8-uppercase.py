#!/usr/bin/python3
def uppercase(str):
    string = ""
    for idx in range(len(str)):
        c = str[idx]
        if (ord(c) in range(97, 123)):
            c = chr(ord(c) - 32)
        string += c
    print("{}".format(string))
