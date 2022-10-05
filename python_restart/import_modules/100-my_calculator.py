#!/usr/bin/python3

if __name__ == "__main__":
    from os import sys
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if sys.argv[2] not in ['+','-','*','/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    from calculator_1 import add, sub, mul, div
    a,b = int(sys.argv[1]), int(sys.argv[3])

    if sys.argv[2] == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    if sys.argv[2] == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    if sys.argv[2] == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    if sys.argv[2] == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
