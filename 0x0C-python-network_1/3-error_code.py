#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8)
"""
from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv


if __name__ == '__main__':
    try:
        with urlopen(argv[1]) as response:
            body = response.read()
            decodedbody = body.decode("utf-8")
            print(decodedbody)
    except HTTPError as error:
        print("Error code: {}".format(error.code))
