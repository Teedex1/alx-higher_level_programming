#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 'a' <= i <= 'z':
            i = chr(ord(i) - ord('a') + ord('A'))
            print("{}".format(i), end="")
    print()
