#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
result_addition = add(a, b)
result_subtraction = sub(a, b)
result_multiplication = mul(a, b)
result_division = div(a, b)
print("{} + {} = {}".format(a, b, result_addition))
print("{} - {} = {}".format(a, b, result_subtraction))
print("{} * {} = {}".format(a, b, result_multiplication))
print("{} / {} = {}".format(a, b, result_division))
