#!/usr/bin/python3
from sys import argv


def main():
    sum = 0
    for arg in argv:
        if arg != argv[0]:
            arg = int(arg)
            sum = sum + arg
    print("{}".format(sum))


if __name__ == '__main__':
    main()
