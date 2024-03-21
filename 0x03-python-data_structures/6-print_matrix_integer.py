#!/usr/bin/python3
'''
print_matrix_integer: function that prints integers from input matrix
print one row per line
'''

def print_matrix_integer(matrix=[[]]):
    # iterate through my_list
    for elem in my_list:
        for item in elem:
            if item is not elem[-1]:
                print("{:d}".format(item), end=" ")
            else:	    
                print("{:d}".format(item))


if __name__ == '__main__':
    print_matrix_integer(matrix=[[]])
