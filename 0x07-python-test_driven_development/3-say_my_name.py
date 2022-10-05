#!/usr/bin/python3
"""This function prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """Prints the first and the last name passed to the module
    Raises:
        TypeError if firstname or lastname is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
