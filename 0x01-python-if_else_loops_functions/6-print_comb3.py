#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print("{0}{1}".format(i, j))
        else:
            print("{0}{1}".format(i, j), end=", ")
