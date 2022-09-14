#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}\n".format(value))
        return True
    except(TypeError, ValueError):
        print("Exception: {}".format(sys.exec_info()[1]), file=sys.stderr)
        return False
