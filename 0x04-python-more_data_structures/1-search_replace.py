#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for i in new_list:
        if i == search:
            new_list[i - 1] = replace
    return new_list
    """
    new_list[search - 1] = replace
    return new_list
    """
