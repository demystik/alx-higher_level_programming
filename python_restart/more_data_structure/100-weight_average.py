#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    lst = my_list.copy()
    sum1 = sum2 = 0
    for tup in my_list:
        sum1 += (tup[0] * tup[1])
        sum2 += tup[1]
    return (sum1 / sum2)
