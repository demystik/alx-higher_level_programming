#!/usr/bin/python3

if __name__ == "__main__":
    from os import sys
    sum = 0
    for i in range(len(sys.argv) - 1):
        sum += int(sys.argv[i + 1])
    print(f"{sum}")
