#!usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    idx_end = len(my_list) - 1
    for number in range(len(my_list)):
        print("{:d}".format(my_list[idx_end]))
        idx_end -= 1
