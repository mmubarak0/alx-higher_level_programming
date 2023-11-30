#!/bin/bash
# displays all HTTP methods the server will accept.
curl -sI $1 | tail -n2 | head -n1 | cut -d" " -f1 --complement;
