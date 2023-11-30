#!/bin/bash
#This list the list of allowed methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
