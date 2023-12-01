#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status using urllib.
It includes a token in the request headers and displays the body of the response in a specific format.
"""

import urllib.request as ur

url = 'https://intranet.hbtn.io/status'
token = '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'
headers = {'Authorization': f'token {token}', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0'}

req = ur.Request(url, headers=headers)

with ur.urlopen(req) as res:
    res = res.read()
    print('Body response:$')
    print('\t- type: {}$'.format(type(res)))
    print('\t- content: {}$'.format(res))
    print('\t- utf8 content: {}$'.format(str(res, 'utf-8')))

