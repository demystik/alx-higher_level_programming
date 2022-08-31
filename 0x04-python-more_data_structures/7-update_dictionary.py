#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for keyy in a_dictionary:
        if keyy == key:
            a_dictionary[key] = value
            return a_dictionary
    a_dictionary[key] = value
    return a_dictionary
