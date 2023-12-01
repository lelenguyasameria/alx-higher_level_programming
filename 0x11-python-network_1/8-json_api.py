#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    payload = {'q': q}
    
    try:
        response = requests.post(url, data=payload)
        data = response.json()

        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")

