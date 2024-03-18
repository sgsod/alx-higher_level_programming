#!/usr/bin/python3
'''
print_list_integer: function that prints integers from input list
print one element per line
'''


def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    # iterate through my_list
    for elem in my_list:
        print("{:d}".format(elem))
    my_list.reverse()


if __name__ == '__main__':
    print_list_integer(my_list=[])
