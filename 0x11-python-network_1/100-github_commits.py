#!/usr/bin/python3
""" lists 10 most recent commits from a repo"""

from sys import argv
import requests

if __name__ == "__main__":
    git = argv[1]
    name = argv[2]
    link = "https://api.github.com/repos/{}/{}/commits".format(name, git)
    req = requests.get(link)
    if req.status_code != 200:
        print("Error code: {}".format(req.status_code))
    else:
        for idx in req.json()[:10]:
            print("{}: {}".format(idx.get("sha"),
                  idx.get("commit").get("author").get("name")))
