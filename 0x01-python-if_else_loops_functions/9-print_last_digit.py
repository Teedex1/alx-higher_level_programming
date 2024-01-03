#!/usr/bin/python3
def print_last_digit(number):
    if num < 0:
        last_digit = num % -(10)
        print(-(last_digit), end='')
    else:
        last_digit = number % 10
        print(last_digit, end='')
    return abs(last_digit)
