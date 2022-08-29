#!/usr/bin/python3

if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    operator = ""
    operator = sys.argv[2]
    op_dic = {"*": mul, "-": sub, "+": add, "/": div}
    if operator not in list(op_dic.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    n1 = int(sys.argv[1])
    n2 = int(sys.argv[3])
    print("{} {} {} = {}".format(n1, operator, n2, op_dic[operator](n1, n2)))
