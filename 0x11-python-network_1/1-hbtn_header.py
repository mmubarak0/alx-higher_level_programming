#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id."""

import urllib.request as request
import sys

with request.urlopen(sys.argv[1]) as response:
    content = response.getheader("X-Request-Id")
    print(f"{content}")
