#!/usr/bin/python3
def print_last_digit(number):
# calculate the last digit and store in last_digit
    if number >= 0:
        last_digit = number % 10
    else:
        last_digit = number % -10
# print last digit
    print("{}".format(last_digit), end="")
    return last_digit
