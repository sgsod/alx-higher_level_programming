#!/usr/bin/python3
for i in range(99):
    print("{:0>2}".format(i), end=", ")
# 99 is not accessed in for loop
print("{}".format(i + 1))
