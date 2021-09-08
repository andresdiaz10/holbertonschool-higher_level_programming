#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 0
    argc = len(sys.argv) - 1
    if (argc == 0):
        print("0 arguments.")
    elif (argc != 1):
        print("{} arguments:".format(argc))
    else:
        print("1 argument:")
    for i in range(argc):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
