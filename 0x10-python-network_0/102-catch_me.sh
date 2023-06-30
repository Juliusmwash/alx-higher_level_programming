#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response.
response=$(curl -s 0.0.0.0:5000/catch_me --output /dev/null --write-out "%{http_code}"); if [ "$response" -eq 200 ]; then printf "You got me!"; fi
