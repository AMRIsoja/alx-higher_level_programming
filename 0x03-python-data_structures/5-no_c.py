#!/usr/bin/python3

def no_c(my_string):
    str_nc = ""
    for character in my_string:
        if character == 'c' or character == 'C':
            continue
        str_nc += character
    return str_nc
