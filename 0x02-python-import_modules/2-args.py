#!/usr/bin/python3

if __name__ == "__main__":
    import sys
arg = sys.argv
lenght = len(arg) - 1
if lenght == 0:
    print("{} arguments.".format(lenght))
elif lenght == 1:
    print("{} argument:".format(lenght))
    print("{}: {}".format((lenght), arg[1]))
else:
    print("{}: argument:".format(lenght))
    for i in range(lenght + 0):
        print("{}: {}".format((i + 1), arg[i + 1]))
