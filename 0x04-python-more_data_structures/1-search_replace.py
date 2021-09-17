#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list[0:]
    for i in range(len(new)):
        if new[i] == search:
            new[i] = replace
    return (new)
