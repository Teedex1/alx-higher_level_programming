#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastdigit = number % -10
else:
    lastdigit = number % 10
message = "Last digit of {:d} is {:d}".format(number, lastdigit)
if lastdigit > 5:
    print(message + " and is greater than 5")
elif lastdigit < 6 and lastdigit != 0:
    print(message + " and is less than 6 and not 0")
else:
    print(message + " and is 0")
