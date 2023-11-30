#!/bin/bash
#This is this it
curl -s -o /dev/null -w "%{http_code}" "$1"
