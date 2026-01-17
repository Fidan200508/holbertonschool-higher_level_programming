#!/usr/bin/python3
"""
This module defines the MyList class.
"""


class MyList(list):
    """A class that inherits from list"""

    def print_sorted(self):
        """Prints the list in ascending order
         without modifying the original list"""
        print(sorted(self))

