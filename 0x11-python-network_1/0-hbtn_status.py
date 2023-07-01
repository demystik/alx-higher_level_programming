#!/usr/bin/python3
"""This script fetches https://alx-intranet.hbtn.io/status"""
from urllib import request


if __name__ == "__main__":
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        resp_file = response.read()
        decoded_file = resp_file.decode("utf-8")
    print(decoded_file)
