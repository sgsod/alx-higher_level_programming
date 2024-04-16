#!/usr/bin/python3
"""Contains class Mylist"""


class MyList(list):
    """list descendant"""

    def __init__(self):
        """initialising instance"""
        super().__init__()

    def print_sorted(self):
        """print soted list"""
        print(sorted(self))
