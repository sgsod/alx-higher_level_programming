#!/usr/bin/python3
"""contains function append_write"""


def write_file(filename="", text=""):
    """append text and return number of chaacters"""

    with open(filename, 'a', encoding="utf-8") as s:
        count = s.write(text)
    return count
