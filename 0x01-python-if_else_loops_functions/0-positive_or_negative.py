#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# if the number is greater than 0
if number > 0:
 print(f"{number:d} is positive")
# if the number is equal to zero
elif number == 0:
 print(f"{number:d} is zero")
# if the number is less than 0
else:
 print(f"{number:d} is negative")
