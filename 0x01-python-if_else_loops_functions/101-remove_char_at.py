#!/usr/bin/python3
def remove_char_at(str, n):
    res = ""
    for character in range(0, len(str)):
        if character != n:
            res = res + str[character]
    return res
