#!/usr/bin/python3
"""contains function read_file"""


def read_file(filenamme=""):
    """read and pint file"""

    with open(filename, encoding="utf-8") as s:
        print("{:s}".format(filename.read()))
