#!/usr/bin/python3
""" uses urllib to geta url"""

import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}\n\t- content: {}".format(type(html), html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
