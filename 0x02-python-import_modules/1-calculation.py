#!/usr/bin/python3
import calculator_1 as solve


def main():
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, solve.add(a, b)))
    print("{} - {} = {}".format(a, b, solve.sub(a, b)))
    print("{} * {} = {}".format(a, b, solve.mul(a, b)))
    print("{} / {} = {}".format(a, b, solve.div(a, b)))


if __name__ == '__main__':
    main()
