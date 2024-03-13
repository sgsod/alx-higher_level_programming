#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10
# if the last digit is greater than 5
if last_digit > 5:
    print(f"Last digit of {number:d} is {last_digit:d} and is greater than 5")
# if the last digit is equal to zero
elif last_digit == 0:
    print(f"Last digit of {number:d} is {last_digit:d} and is 0")
# if the last digit is less than 6 and not zero
else:
    print(f"Last digit of {number:d} is {last_digit:d}\
 and is less than 6 and not 0")
