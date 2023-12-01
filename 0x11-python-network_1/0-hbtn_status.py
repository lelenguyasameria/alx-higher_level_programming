#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status using urllib.
It displays the body of the response in a specific format.
"""

import urllib.request as ur

url = 'https://alx-intranet.hbtn.io/status'

with ur.urlopen(url) as response:
    body = response.read()
    print('Body response:')
    print('\t- type: {}'.format(type(body)))
    print('\t- content: {}'.format(body.decode('utf-8')))

