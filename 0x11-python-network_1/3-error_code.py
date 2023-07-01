#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)."""

if __name__ == "__main__":
    import sys
    from urllib import request, error
    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            print(response.read().decode('UTF-8'))
    except error.HTTPError as error:
        print("Error code:", error.code)
