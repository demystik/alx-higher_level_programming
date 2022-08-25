#!/usr/bin/python3
def uppercase(str):
    bol = ""
    for i in range(0, len(str)):
        bol = 0
        for j in range(97, 123):
            if str[i] == chr(j):
                print("{}".format(chr(j - 32)), end="")
                bol = 1
        if bol != 1:
            print("{}".format(str[i]), end="")
        if i == len(str) - 1:
            print("")
