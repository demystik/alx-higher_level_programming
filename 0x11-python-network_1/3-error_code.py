#!/usr/bin/python3
"""A script that takes in a URL, send a request to the URL
and displays the body response
"""

if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('UTF-8'))
        except error.HTTPError as er:
            print("Error code:", er.code)
