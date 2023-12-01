#!/usr/bin/python3
"""
This script takes in a URL, sends a request, and displays the value of the X-Request-Id variable in the header.
"""

import urllib.request as ur
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with ur.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)

