#!/usr/bin/python3
import sys
if __name__ == "__main__":
    num_args = len(sys.argv) - 1

    print("{} argument{}{}".format(
        num_args,
        's' if num_args != 1 else '',
        ':' if num_args > 0 else '.'
        ))
    for i in range(num_args):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
