#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total_sum = 0
    num_args = len(sys.argv)

    for i in range(1, num_args):
        total_sum += int(sys.argv[i])

    print("{}".format(total_sum))
