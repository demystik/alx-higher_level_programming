#!/usr/bin/python3
"""This function prints a square with the character #"""


def print_square(size):
    """prints a square with the character #
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
        TypeError: if size is float and is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
