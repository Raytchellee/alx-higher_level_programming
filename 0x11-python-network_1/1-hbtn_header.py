#!/usr/bin/python3
""" displays X-Request-Id gotten from url response header"""

from sys import argv
from urllib import request


if __name__ == "__main__":
    with request.urlopen(argv[1]) as r:
        print(r.getheader("X-Request-Id"))
