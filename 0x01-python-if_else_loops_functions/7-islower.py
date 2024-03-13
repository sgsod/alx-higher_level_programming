#!/usr/bin/python3
def islower(c):
    match c:
        case c >= 97 and c <= 122:
            return True
        case _:
            return False
