#!/usr/bin/python3
"""placeholder"""


def write_file(filename="", text=""):
    """write file"""
    with open(filename, 'w', encoding="utf-8") as ace:
        ace.write(text)
    return len(text)
