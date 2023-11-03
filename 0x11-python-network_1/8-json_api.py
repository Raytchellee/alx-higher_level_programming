#!/usr/bin/python3
""" sends a letter as a payload to a request url """

from sys import argv
import requests

if __name__ == "__main__":
    link = 'http://0.0.0.0:5000/search_user'

    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]
    datum = {'q': q}
    req = requests.post(link, data=datum)
    try:
        obj = req.json()
        if len(obj) == 0:
            print("No result")
        else:
            print("[{}] {}".format(obj['id'], obj['name']))
    except ValueError:
        print("Not a valid JSON")
