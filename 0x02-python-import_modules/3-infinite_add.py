#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    s = 0
    for i in sys.argv[1:]:
        s += int(i)
    print(s)
