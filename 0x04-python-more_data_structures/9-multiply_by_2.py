#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dico = a_dictionary.copy()
    for i in dico:
        dico[i] *= 2
    return dico
