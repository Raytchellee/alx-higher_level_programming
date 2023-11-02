#!/bin/bash
#sends a request to an input uri and displays size of response
curl -sL -X PUT -d "user_id=98" -H "Origin:HolbertonSchool" 0.0.0.0:5000/catch_me
