#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list.reverse()
        get = len(my_list)
        for i in range(get):
            print("{:d}".format(my_list[i]))
