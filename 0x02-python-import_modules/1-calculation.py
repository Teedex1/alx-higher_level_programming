#!/usr/bin/python3
if __name__=="__main__":
    import calculator_1 #import add, sub, mul, div
    a = 10
    b = 5
    result_addition = calculator_1.add(a, b)
    result_sutraction = calculator_1.sub(a, b)
    result_multiplication = calculator_1.mul(a, b)
    result_division = calculator_1.div(a, b)
    print("{} + {} = {}".format(a, b, result_addition))
    print("{} - {} = {}".format(a, b, result_sutraction))
    print("{} * {} = {}".format(a, b, result_multiplication))
    print("{} / {} = {}".format(a, b, result_division))
