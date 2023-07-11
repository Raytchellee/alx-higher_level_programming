#!/usr/bin/python3
for idx in range(97, 123):
    if (chr(idx) != 'e' and chr(idx) != 'q'):
        print("{}".format(chr(idx)), end="")
