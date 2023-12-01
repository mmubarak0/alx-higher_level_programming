#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter."""

if __name__ == "__main__":
    import sys
    import urllib.request as request
    import urllib.parse as parse

    values = {'email': sys.argv[2]}
    req = request.Request(sys.argv[1], parse.urlencode(values).encode('ascii'))
    with request.urlopen(req) as response:
        content = response.read()
        print(content.decode('utf-8'))
