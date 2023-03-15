#!/usr/bin/python3
"""
Python script that takes
in a URL and an email, sends
a POST request to the passed URL
with the email as a parameter, and
displays the body of the response (decoded in utf-8)
"""
from urllib.request import urlopen
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data_dict = {'email': email}
    utf8data = urlencode(data_dict).encode("utf-8")

    with urlopen(url, data=utf8data) as response:
        body = response.read()
        print(body.decode("utf-8"))
