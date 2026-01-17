#!/usr/bin/python3
"""This module defines the MyList class."""


class MyList(list):
    """A class that inherits from list."""

    def print_sorted(self):
        """Print the list in ascending order without modifying it."""
        print(sorted(self))
