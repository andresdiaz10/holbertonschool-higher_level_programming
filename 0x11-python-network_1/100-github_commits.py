#!/usr/bin/python3
'''List 10 commits'''
from sys import argv
import requests


if __name__ == "__main__":
    response = requests.get("https://api.github.com/repos/{}/{}/commits"
                            .format(argv[2], argv[1]))
    resBody = response.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                resBody[i].get("sha"), resBody[i].get("commit").
                get("author").get("name")))
    except Exception:
        pass
