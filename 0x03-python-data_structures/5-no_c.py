#!/usr/bin/env python3


def no_c(my_string):
    # iterate through string
    new_string = ""
    for st in my_string:
    # for each character find out if there is c or C
        if st != 'c' and st != 'C':
            new_string = new_string + st
    return new_string


if __name__ == '__main__':
    no_c(my_string)
