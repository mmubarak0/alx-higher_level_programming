#!/usr/bin/python3
"""Load add save."""

import json
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file")\
    .load_from_json_file


try:
    ll = load_from_json_file("add_item.json")
except Exception:
    ll = []
for arg in sys.argv[1:]:
    ll.append(arg)
save_to_json_file(ll, "add_item.json")
