#!/usr/bin/python3
""" posts mail and display response body """

import requests
from sys import argv

if __name__ == "__main__":
    link = argv[1]
    mail = argv[2]
    datum = {'email': mail}
    req = requests.post(link, data=datum)
    print(req.text)
