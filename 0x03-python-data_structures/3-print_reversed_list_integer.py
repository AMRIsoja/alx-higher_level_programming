#!usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list:
        if len(my_list) > 0:
            last_idx = len(my_list) - 1
            for number in range(len(my_list)):
                print("{}".format(my_list[last_idx]))
                last_idx -= 1
