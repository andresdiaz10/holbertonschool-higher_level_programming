#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)
    weight = 0
    average = 0
    for i in my_list:
        average += (i[0] * i[1])
        weight += i[1]
    return (average / weight)
