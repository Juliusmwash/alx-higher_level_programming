#!/usr/bin/python3
""" Fetches https://alx-intranet.hbtn.io/status """
import urllib.request

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    content = response.read()

body_response = content.decode("utf-8")

print("Body response:")
print("    - type:", type(content))
print("    - content:", content)
print("    - utf8 content:", body_response)
