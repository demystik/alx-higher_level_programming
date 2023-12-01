#!/usr/bin/python3
"""This python script takes in a URL, sends a request to the URL
and displays the value of the 'X-Request-Id' variable found in the header"""
import sys
from urllib import request

if __name__ == "__main__":
    args = sys.argv[1]
    with request.urlopen(args) as resp:
        print(resp.headers["X-Request-Id"])
