#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    s = 0
    for i in range(0, x):
        try:
            s += 1
            print("{:d}".format(my_list[i]), end="")
        except IndexError as e:
            s -= 1
            raise e
        except Exception:
            s -= 1
            continue
    print()
    return s
