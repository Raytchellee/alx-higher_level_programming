#!/bin/bash
#sends a request to an input uri and displays size of response
curl -sI "$1" | grep -i "Allow:" | cut -d " " -f 2-
