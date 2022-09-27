#!/usr/bin/python3
"""Defines an instance of a class function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a given class."""
    if isinstance(obj, a_class):
        return True
    else:
        return False
