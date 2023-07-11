#!/usr/bin/python3
for idx in range(0, 100):
    if (idx % 10 > idx // 10):
        if (idx != 89):
            print("{:02d}, ".format(idx), end="")
        else:
            print("{}".format(idx))
