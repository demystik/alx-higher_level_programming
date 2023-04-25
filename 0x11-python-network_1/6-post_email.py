#!/usr/bin/python3

"""pt that takes in a URL and an email address, sends a POST request to the
passed URL with the email as a parameter, and
finally displays the body of the response
"""
import sys
import urllib.request

if __name__ == "__main__":
        url = sys.argv[1]
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as resp:
            print(dict(response.headers).get("X-Request-Id"))
