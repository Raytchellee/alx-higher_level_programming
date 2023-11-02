#!/bin/bash
#sends a request to an input uri and displays size of response
curl -sX POST -H "Content-Type: application/json" --data @"$2" "$1"
