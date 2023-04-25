#!/usr/bin/python3
"""This python script takes a URL as an args
send a request and displays the value of the 
X-Request-Id variable found in the header of the response
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as resp:
        print(dict(resp.headers).get("X-Request-Id"))
