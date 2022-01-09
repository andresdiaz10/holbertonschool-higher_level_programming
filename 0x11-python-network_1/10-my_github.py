#!/usr/bin/python3
'''that takes your GitHub credentials (username and password) and
uses the GitHub API to display your id'''
from sys import argv
import requests


if __name__ == "__main__":
    response = requests.get("https://api.github.com/user", auth=(argv[1], argv[2]))
    print(response.json().get("id"))
