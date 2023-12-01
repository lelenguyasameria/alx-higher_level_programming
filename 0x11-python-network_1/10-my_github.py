#!/usr/bin/python3
"""
This script takes your GitHub credentials (username and personal access token) and uses the GitHub API to display your id.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./script.py <username> <personal_access_token>")
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    url = 'https://api.github.com/user'

    headers = {
        'Authorization': 'Basic {}:{}'.format(lelenguyasameria, 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),
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        if 'id' in data:
            print("Your GitHub id is: {}".format(data['id']))
        else:
            print("Unable to retrieve GitHub id. Check your credentials.")

    except ValueError:
        print("Not a valid JSON. Check your credentials.")

