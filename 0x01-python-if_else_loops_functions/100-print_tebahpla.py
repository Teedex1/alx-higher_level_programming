#!/usr/bin/python3
for i in range(ord('z'), ord('A'), -2):
    print("{}".format(chr(i) + chr(i - 33)), end="")
print()
