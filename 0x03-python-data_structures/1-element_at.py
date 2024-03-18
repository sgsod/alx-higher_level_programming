#!/usr/bin/python3
'''
element_at: returns element from list
'''


def element_at(my_list, idx):
    # get length of list
    list_len = len(my_list)
    # if idx is invalid ret
    if idx >= list_len or idx < 0:
        return None

    else:
        return my_list[idx]


if __name__ == '__main__':
    element_at(my_list, idx)
