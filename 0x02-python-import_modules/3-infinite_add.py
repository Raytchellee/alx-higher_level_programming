#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    length = len(argv)
    total = 0

    for idx in range(1, length):
        total += int(argv[idx])
    print("{}".format(total))
