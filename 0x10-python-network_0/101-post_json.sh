#!/bin/bash
#this file does this and that
curl -s -H "Content-Type: application/json" -d "$(cat $2)" "$1"

