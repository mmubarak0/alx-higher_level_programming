#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id."""

if __name__ == "__main__":
    import sys
    import urllib.request as request
    import urllib.parse as parse

    values = {'name': 'Michael Foord'}
    req = request.Request(sys.argv[1], parse.urlencode(values).encode('ascii'))
    with request.urlopen(sys.argv[1]) as response:
        content = response.getheader("X-Request-Id")
        print(content)
