#!/usr/bin/env bash
# This script taske a URL, send a request, & displays the size of content
curl -s "$1" | wc -c