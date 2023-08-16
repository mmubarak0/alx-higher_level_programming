#!/usr/bin/python3
def uniq_add(my_list=[]):
    if type(my_list) is list:
        uniq = set(my_list)
        return sum(uniq)
