#!/usr/bin/python3

def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        print(i, end="")
    print("")

uppercase("best")
uppercase("Best School 98 Battery street")
