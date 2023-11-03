#!/usr/bin/python3
""" gets header value """

from sys import argv
import requests

if __name__ == "__main__":
    req = requests.get(argv[1])
    print(req.headers.get('X-Request-Id'))
