#!/usr/bin/python3
''' POST request to http://0.0.0.0:5000/search_user with the
letter as a parameter.'''
from sys import argv
import requests

if __name__ == "__main__":
    reqBody = {"q": ""}
    if len(argv) != 2:
        response = requests.post("http://0.0.0.0:5000/search_user", reqBody)
    else:
        reqBody["q"] = argv[1]
        response = requests.post("http://0.0.0.0:5000/search_user", reqBody)
    try:
        resBody = response.json()
        if resBody == {}:
            print("No result")
        else:
            print("[{}] {}".format(resBody.get("id"), resBody.get("name")))
    except ValueError:
        print("Not a valid JSON")
