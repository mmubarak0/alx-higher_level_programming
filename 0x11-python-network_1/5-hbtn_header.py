#!/usr/bin/python3
"""Sends a request to the URL and displays value of X-Request-Id."""

if __name__ == "__main__":
    import requests
    import sys

    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.post(sys.argv[1], data=payload)
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
