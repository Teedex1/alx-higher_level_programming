#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
        print("Inside result: {}".format(div))
    else:
        print("Inside result: {:.1f}".format(div))
    return div