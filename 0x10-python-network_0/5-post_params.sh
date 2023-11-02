#!/bin/bash
#sends a request to an input uri and displays size of response
curl -sX POST -d "email=test@gmail.com&subject=I+will+always+be+here+for+PLD" "$1"
