#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)."""

import sys
from urllib import request, error

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url, timeout=10) as response:
            body = response.read.decode('utf-8')
            print(body)
    except error.HTTPError as error:
        print("Error code", error.code)
