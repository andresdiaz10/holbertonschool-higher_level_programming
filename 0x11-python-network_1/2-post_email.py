#!/usr/bin/python3
"""POST Email"""

from sys import argv
import urllib.request
import urllib.parse


if __name__ == "__main__":
    client = argv[1]
    reqBody = {"email": argv[2]}
    reqData = urllib.parse.urlencode(reqBody).encode("ascii")
    request = urllib.request.Request(client, reqData)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
