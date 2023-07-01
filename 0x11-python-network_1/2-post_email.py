#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body
of the response (decoded in utf-8)"""

import sys
from urllib import request, parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_req = (url, email)

    def send_post_request(url, email):
        data = parse.urlencode({'email': email}).encode('utf-8')
        request = urllib.request.Request(url, data=data, methon='POST')
        with request.urlopen(request) as response:
            body = response.read().decode('utf-8')
            print(body)