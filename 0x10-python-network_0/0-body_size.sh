#!/bin/bash
# This script takes in a URL, sends a request to that URL,
#+	and displays the size of the body of the response

# Check if a URL is provided as an argument
if [ $# -eq 0 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Store the URL argument
url=$1

# Send the request and retrieve the response body
response=$(curl -sI "$url" | grep -i Content-Length | awk '{print $2}' | tr -d '\r')

# Check if the response body size is available
if [ -z "$response" ]; then
  echo "Unable to retrieve the response body size."
  exit 1
fi

# Display the response body size in bytes
echo "$response"

