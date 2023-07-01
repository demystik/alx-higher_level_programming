#!/bin/bash
#This is this it
echo $(curl -s -o /dev/null -w "%{http_code}" 18.207.3.56)
