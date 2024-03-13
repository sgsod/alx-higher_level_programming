#!/usr/bin/python3
def islower(c):
    match c:
        case ord(c) >= 97 and ord(c) <= 122:
            return True
        case _:
            return False
