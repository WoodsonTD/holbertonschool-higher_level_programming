#!/usr/bin/python3
"""json"""
import json


def save_to_json_file(my_obj, filename):
    "save json"
    with open(filename, 'w') as ace:
        json.dump(my_obj, ace)
