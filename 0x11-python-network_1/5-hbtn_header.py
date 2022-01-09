#!/usr/bin/python3
'''X request id in response header'''
from sys import argv
import requests

if __name__ == "__main__":
    response = requests.get(argv[1])
    print(response.headers.get("X-Request-Id"))
