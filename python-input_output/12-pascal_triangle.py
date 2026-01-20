#!/usr/bin/python3
"""a function that returns a list of lists of integers
 representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """a function that returns a list of lists of integers
     representing the Pascal’s triangle of n"""
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            for j in range(1, len(last_row)):
                row.append(last_row[j-1] + last_row[j])
            row.append(1)
        triangle.append(row)
    return triangle
