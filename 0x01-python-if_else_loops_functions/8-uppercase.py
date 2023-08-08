#!/usr/bin/python3
def uppercase(str):
    for i in str:
        i = chr(ord(i) - abs(ord('A') - ord('a'))) if\
            (ord(i) >= ord('a') and ord(i) <= ord('z')) else i
        print("{}".format(i), end="")
    print()
