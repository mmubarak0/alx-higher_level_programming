#!/usr/bin/python3
"""Script that fetches https://alx-intranet.hbtn.io/status."""

if __name__ == "__main__":
    import requests

    r = requests.get('https://alx-intranet.hbtn.io/status')
    content = r.text
    content_type = type(content)
    print("Body response:")
    print(f"\t- type: {content_type}")
    print(f"\t- content: {content}")
