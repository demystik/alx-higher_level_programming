#!/usr/bin/python3
alph = 122
while(alph >= 97):
    print(chr(alph) if alph % 2 == 0 else chr(alph - 32), end="")
    alph -= 1
