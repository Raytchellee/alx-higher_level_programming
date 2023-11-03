#!/usr/bin/python3
""" fetches status using requests """

import requests

if __name__ == "__main__":
    req = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:\n\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
