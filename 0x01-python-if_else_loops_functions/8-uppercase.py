#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            str2 = ord(c) - 32
        else:
            str2 = ord(c)
        print("{}".format(chr(str2)), end="")
    print("")
