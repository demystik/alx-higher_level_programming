#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

    num1 = int(sys.argv[1])
    num2 = int(sys.argv[3])
    operator = ""
    operator = sys.argv[2]

    op_dic = {"*": mul, "-": sub, "+": add, "/": div}
    if operator not in list(op_dic.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(num1, operator, num2, op_dic[operator](num1, num2)))
