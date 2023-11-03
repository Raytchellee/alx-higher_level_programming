#!/usr/bin/python3
""" posts an email to the email variable parsed """

from sys import argv
from urllib import request, parse

if __name__ == "__main__":
    link = argv[1]
    mail = argv[2]

    payload = parse.urlencode({'email': mail})
    payload = payload.encode('ascii')
    with request.urlopen(link, payload) as r:
        print(r.read().decode('utf-8'))
