#!/usr/bin/python3
"""json"""
import json


def load_from_json_file(filename):
    "load from json"
    with open(filename) as ace:
        return json.load(fred)
