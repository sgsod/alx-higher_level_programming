#!/usr/bin/python3
"""contains function write_file"""


def write_file(filename="", text=""):
    """write and return"""

    with open(filename, 'w', encoding="utf-8") as s:
        count = s.write(text)
    return count
