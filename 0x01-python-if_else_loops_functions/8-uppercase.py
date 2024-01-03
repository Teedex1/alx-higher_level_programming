#!/usr/bin/python3
def uppercase(input_str):
    for char in input_str:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - 32)
            print("{}".format(char), end="")
    print()
