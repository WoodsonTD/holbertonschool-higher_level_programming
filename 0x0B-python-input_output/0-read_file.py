#!/usr/bin/python3
"""placeholder"""


def read_file(filename=""):
    """file read"""
    with open(filename, encoding="utf-8") as ace:
        print(ace.read(), end="")
