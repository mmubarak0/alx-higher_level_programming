#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    len_argv = len(sys.argv)
    argv = sys.argv
    ops = {'+': add, '-': sub, '*': mul, '/': div}

    if len_argv != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] not in ops.keys():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    result = ops[argv[2]](int(argv[1]), int(argv[3]))
    print(f"{argv[1]} {argv[2]} {argv[3]} = {result}")
