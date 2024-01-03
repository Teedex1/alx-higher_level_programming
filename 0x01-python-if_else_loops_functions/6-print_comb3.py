#!/usr/bin/python3
for x in range(9):
    for y in range(x + 1 if x > 0 else 1, 10):
        print('{}{}, '.format(x, y), end='')
print('89')
