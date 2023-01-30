#!/usr/bin/python3
"""placeholder"""


def inherits_from(obj, a_class):
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return true
    return false
