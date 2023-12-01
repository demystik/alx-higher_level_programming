#!/usr/bin/python3
"""
Python script that fetches 
https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":

    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        resp = response.read()
    print("Body response:")
    print(f"\t - type: {type(resp)}")
    print(f"\t - content: {resp}")
    print(f"\t - utf8 content: {body.decode('utf-8')}")
