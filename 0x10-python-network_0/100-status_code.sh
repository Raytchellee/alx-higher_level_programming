#!/bin/bash
#sends a request to an input uri and displays size of respons
curl -s -o /dev/null -w "%{http_code}" "$1"
