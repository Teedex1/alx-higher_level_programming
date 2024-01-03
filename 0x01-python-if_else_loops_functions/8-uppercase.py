#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        if 97 <= ord(i) <= 122:
            i = chr(ord(i) - 32)
        result += i
    print("{}".format(result))
