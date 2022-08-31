#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(my_list)
    result = 0
    for i in new:
        result += i
    return result
