#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""

import urllib.request as request

with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    content = response.read()
    content_type = type(content)
    utf8_content = content.decode('utf-8')
    print("Body response:")
    print(f"\t- type: {content_type}")
    print(f"\t- content: {content}")
    print(f"\t- utf8 content: {utf8_content}")
