#!/usr/bin/python3
for i in range(ord('z'), ord('A') - 1, -2):
    if i >= ord('a'):
        print("{}".format(chr(i) + chr(i - 33)), end="")
print()
