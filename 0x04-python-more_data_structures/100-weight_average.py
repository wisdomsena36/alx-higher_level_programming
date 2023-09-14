#!/usr/bin/python3
def weight_average(my_list=[]):
    result = sum([x[0] * x[1] for x in my_list]) / \
            (sum([x[1] for x in my_list]) or 1)
    return (result)
