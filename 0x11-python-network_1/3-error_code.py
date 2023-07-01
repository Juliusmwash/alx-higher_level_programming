#!/usr/bin/python3
"""
Sends a request to the URL and displays the body of the
response (decoded in utf-8).
"""
import urllib.request
import urllib.error
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)


if __name__ == "__main__":
    main()
