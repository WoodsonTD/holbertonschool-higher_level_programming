#!/usr/bin/python3
"""placeholder"""


def append_write(filename="", text=""):
    """file append"""
    with open(filename, 'a', encoding="utf-8") as ace:
        return ace.write(text)
