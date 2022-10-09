#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        print("Exception: {}".format(sys.exec_info()[1]), file=sys.stderr)
        #print("Exception: {}".format(sys.exec_info()[1]), file=sys.stderr)


        return False
        