#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set()
    total = 0
    for i in my_list:
        if i not in unique:
            unique.add(i)
            total += i
    return total
