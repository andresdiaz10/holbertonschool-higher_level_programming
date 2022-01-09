#!/usr/bin/python3
'''Http status code'''
from sys import argv
import urllib.request
import urllib.error


if __name__ == "__main__":
    client = argv[1]
    request = urllib.request.Request(client)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as statuscode:
        print("Error code: {}".format(statuscode.code))
