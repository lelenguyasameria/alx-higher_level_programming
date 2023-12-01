#!/usr/bin/python3
"""
This script takes a URL and an email, sends a POST request to the URL with the email as a parameter,
and displays the body of the response (decoded in utf-8).
"""

import urllib.request as ur
import urllib.parse as up
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    data = up.urlencode(data).encode('utf-8')

    with ur.urlopen(url, data=data) as response:
        body = response.read()
        print(body.decode('utf-8'))

