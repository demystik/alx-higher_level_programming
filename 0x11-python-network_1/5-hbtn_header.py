#!/usr/bin/python3

""" Python script that takes in a URL, sends a request to the URL
and displays the value of the variable
X-Request-Id in the response header"""

if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]

    resp = requests.get(url)
    resp_head = resp.headers
    print(resp_head.get("X-Request-Id"))
