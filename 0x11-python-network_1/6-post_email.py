#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response."""

if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]

    response = requests.post(url, data={'email': sys.argv[2]})
    print(response.text)
