#!/usr/bin/python3
def search_replace(my_list, search, replace):
    result = list(map(lambda e: replace if e == search else e, my_list))
    return (result)
