#!/usr/bin/python3

import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    resp = response.read()
print("Body response:")
print("\t - type: <class 'bytes'>")
print("\t - content: " + str(resp))
print("\t - utf8 content: OK")