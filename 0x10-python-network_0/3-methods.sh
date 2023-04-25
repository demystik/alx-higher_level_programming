#!/usr/bin/env bash
# This script takes URL displays all HTTP methods the server will accept
curl -sI -X "$1" | grep "Allow" | tr -d '\r\n' | sed -e 's/Allow: //g'
