#!/usr/bin/python3
'''
element_at: returns element from list
'''


def replace_in_list(my_list, idx, element):
    # get length of list
    list_len = len(my_list)
    # if idx is invalid ret
    if idx >= list_len or idx < 0:
        return my_list

    else:
        my_list[idx] = element
        return my_list


if __name__ == '__main__':
    replace_in_list(my_list, idx, element)
