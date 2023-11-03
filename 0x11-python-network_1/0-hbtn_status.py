#!/usr/bin/python3
""" uses urllib to geta url"""

import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as r:
        text = r.read()
        print("Body response:")
        print("\t- type: {}\n\t- content: {}".format(type(text), text))
        print("\t- utf8 content: {}".format(text.decode('utf-8')))
