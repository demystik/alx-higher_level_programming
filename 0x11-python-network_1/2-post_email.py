#!/usr/bin/python3

"""Write a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a
parameter"""

if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    data = urllib.parse.urlencode(data).encode('utf-8')


    request = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(request) as response:
        response_data = response.read().decode('utf-8')
        print(response_data)