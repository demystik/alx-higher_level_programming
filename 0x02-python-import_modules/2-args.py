#!/usr/bin/python3

if __name__ == "__main__":
    import sys
arg = sys.argv
lenght = len(arg) - 1
if lenght == 0:
    print("0 arguments.")
elif lenght == 1:
    print("1 argument:")
else:
    print("{}: arguments".format(lenght))
for i in range(lenght + 0):
    print("{}: {}".format((i + 1), arg[i + 1]))
