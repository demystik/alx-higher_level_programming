#!/usr/bin/python3
def roman_to_int(roman_string):

    rom = roman_string
    dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    if not rom in dic:
        return None
    if len(rom) == 1:
        return dic.get(rom)
