#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    cp_list = []
    for i in my_list:
        cp_list.append(my_list[i - 1])
    if idx > i - 1:
        return my_list
    else:
        cp_list[idx] = element
        return cp_list
