#!/bin/bash
#this file does this and that
curl -s -X POST -H "Content-Type: application/json" -d "$(cat $2)" "$1"

