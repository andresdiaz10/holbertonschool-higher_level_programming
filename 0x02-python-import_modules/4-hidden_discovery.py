#!/usr/bin/python3.4
import hidden_4
if __name__ == "__main__":
    for lists in dir(hidden_4):
        if "__" not in lists:
            print(lists)
