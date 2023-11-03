#!/usr/bin/python3
""" requests url and display response body """

from sys import argv
import requests

if __name__ == "__main__":
    link = argv[1]

    req = requests.get(link)
    code = req.status_code
    if code >= 400:
        print("Error code: {}".format(code))
    else:
        print(req.text)
