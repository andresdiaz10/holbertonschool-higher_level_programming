#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    name = list(a_dictionary.keys())[0]
    first_number = a_dictionary[name]
    for key, number in a_dictionary.items():
        if number > first_number:
            first_number = number
            name = key
    return (name)
