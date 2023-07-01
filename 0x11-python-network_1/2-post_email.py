#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body
of the response (decoded in utf-8)
"""

if __name__ == "__main__":
    import sys
    from urllib import request, parse

    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    send_post_req = (url, email)

    def send_post_request(url, email):
        """This function does this and that"""

        content = parse.urlencode(email).encode("ascii")

        request = urllib.request.Request(url, data, method="POST")
        with request.urlopen(request) as response:
            print(response.read().decode("utf-8"))
