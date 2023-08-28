#!/usr/bin/python3
def safe_print_division(a, b):
    n = 0
    result = ""
    try:
        n = a / b
    except Exception:
        n = None
    finally:
        print("Inside result: {}".format(n))
    return n
