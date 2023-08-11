#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list):
        m = my_list[0]
        for i in my_list:
            if i > m:
                m = i
        return m
    return None
