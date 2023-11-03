#!/usr/bin/python3
""" manages error code for url requests """

from sys import argv
from urllib import error, request

if __name__ == "__main__":
    link = argv[1]
    try:
        with request.urlopen(link) as r:
            print(r.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
