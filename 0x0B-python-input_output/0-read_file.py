#!/usr/bin/python3
"""This function reads a text file(UTF8)"""


def read_file(filename=""):
    """open and print utf-8 file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
