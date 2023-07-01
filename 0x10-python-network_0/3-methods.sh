#!/bin/bash
#This list the list of allowed methods
curl -sI -X OPTIONS "$1" 2>&1 | grep "Allow:" | tr -d '\r'
