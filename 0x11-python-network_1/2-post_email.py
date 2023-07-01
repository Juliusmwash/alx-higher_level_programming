#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    # Get the URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Create a data dictionary with the email parameter
    data = {'email': email}
    # Encode the data dictionary as bytes
    data_bytes = urllib.parse.urlencode(data).encode('utf-8')

    # Send the POST request
    with urllib.request.urlopen(url, data=data_bytes) as response:
        # Read the response body and decode it as utf-8
        response_body = response.read().decode('utf-8')

        # Display the response body
        print(response_body)
