#!/usr/bin/python3
'''
new_in_list: changes element at index
'''


def new_in_list(my_list, idx, element):
    # get length of list
    list_len = len(my_list)
    # if idx is invalid ret
    if idx >= list_len or idx < 0:
        return my_list

    else:
        new_list = my_list[:]
        new_list[idx] = element
        return new_list


if __name__ == '__main__':
    new_in_list(my_list, idx, element)
