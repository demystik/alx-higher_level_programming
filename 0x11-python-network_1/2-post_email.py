#!/usr/bin/python3
"""A script that takes in a URL,
then sends a POST request to the passed URL,
takes email as a parameter
and displays the body of the response
"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}
    content = urllib.parse.urlencode(val).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as resp:
        print(resp.read().decode("utf-8"))
