#!/usr/bin/python3
"""

This module is composed by a function that adds two numbers

"""


def add_integer(a, b=98):
    """ Function that adds two integer and/or float numbers

    Args:
        a: first number
        b: second number

    Returns:
        The addition of the two given numbers

    Raises:
        TypeError: If a or b aren't integer and/or float numbers 

    """

    if isinstance(a, int) or isinstance(a, float):
        if isinstance(b, int) or isinstance(b, float):
            a = int(a)
            b = int(b)
            return (a + b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
