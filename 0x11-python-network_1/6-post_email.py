#!/usr/bin/python3
'''Post request'''
from sys import argv
import requests

if __name__ == "__main__":
    reqBody = {"email": argv[2]}
    response = requests.post(argv[1], reqBody)
    print(response.text)
