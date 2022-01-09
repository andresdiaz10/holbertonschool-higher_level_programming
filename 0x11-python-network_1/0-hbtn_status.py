#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body res:")
        print("\t- type: {}".format(type()))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))