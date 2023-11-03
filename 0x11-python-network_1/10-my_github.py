#!/usr/bin/python3
""" connects github and returns id!! """

from sys import argv
import requests

if __name__ == "__main__":
    password = argv[2]
    username = argv[1]
    auth = (username, password)
    req = requests.get('https://api.github.com/user', auth=auth)
    print(req.json().get('id'))
