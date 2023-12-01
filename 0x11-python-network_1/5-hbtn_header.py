#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL, and displays the value of the variable X-Request-Id in the response header.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    
    # Check if X-Request-Id is present in the headers
    if 'X-Request-Id' in response.headers:
        x_request_id = response.headers['X-Request-Id']
        print(x_request_id)
    else:
        print("X-Request-Id not found in the response headers.")

