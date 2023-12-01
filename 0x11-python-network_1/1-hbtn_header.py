#!/usr/bin/python3

import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    resp = response.info()
    varId = resp.get('X-Request-Id')
print(varId)
