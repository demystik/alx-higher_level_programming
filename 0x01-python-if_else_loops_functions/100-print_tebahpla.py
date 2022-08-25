#!/usr/bin/python3
i = 122
while i != 96:
    n = i
    if n % 2 == 1:
        n = ord(chr(n)) - 32
    print("{}".format(chr(n)), end="")
    i = i - 1
