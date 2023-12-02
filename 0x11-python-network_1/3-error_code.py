#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response."""

if __name__ == "__main__":
    import sys
    import urllib.request as request
    import urllib.parse as parse

    req = request.Request(sys.argv[1])

    try:
        with request.urlopen(req) as response:
            content = response.read()
            print(content.decode('utf-8'))
    except Exception as e:
        print(f"Error code: {e.code}")
