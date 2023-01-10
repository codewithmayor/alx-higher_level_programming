#!/usr/bin/python3
"""Module for class MyList"""


class MyList(list):
    """class MyList that inherits from list"""

    def print_sorted(self):
        """Method for print sorted list"""
        print(sorted(self))
