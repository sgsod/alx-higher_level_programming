#!/usr/bin/python3
from sys import argv


def main():
    n = len(argv)
    if n == 1:
        print("0 arguments.")
        return
    elif n == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
        return
    else:
        print("{} arguments:".format(len(argv) - 1))
        n = 1
        for arg in argv:
            if arg != argv[0]:
                print("{}: {}".format(n, arg))
                n = n + 1


if __name__ == '__main__':
    main()
