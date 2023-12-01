#!/usr/bin/python3
"""
This script takes a URL, sends a request to the URL, and displays the body of the response (decoded in utf-8).
It handles urllib.error.HTTPError exceptions and prints the HTTP status code.
"""

import urllib.request as ur
import urllib.error as ue
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with ur.urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except ue.HTTPError as e:
        print("Error code: {}".format(e.code))

