#!/usr/bin/env bash
# curlly port 5000

curl -s -o /dev/null -w '%{size_download}\n' $1;
