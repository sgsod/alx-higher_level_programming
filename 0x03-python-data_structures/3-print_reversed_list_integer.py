#!/usr/bin/python3
'''
print_list_integer: function that prints integers from input list
print one element per line
'''


def print_reversed_list_integer(my_list=[]):
    list_len = len(my_list) - 1
    # iterate through my_list
    while list_len >= 0:
        print("{:d}".format(my_list[list_len]))
        list_len -= 1


if __name__ == '__main__':
    print_list_integer(my_list=[])
