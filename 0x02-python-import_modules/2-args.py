#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    if n == 2:
        print(f"{n - 1} argument:")
    elif n > 1:
        print(f"{n - 1} arguments:")
    else:
        print(f"{n - 1} arguments.")
    for index, word in enumerate(sys.argv):
        if index > 0:
            print("{}: {}".format(index, word))
