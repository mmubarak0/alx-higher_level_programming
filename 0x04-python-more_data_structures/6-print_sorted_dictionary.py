#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if type(a_dictionary) is dict:
        for key in sorted(a_dictionary.keys()):
            print(key + ":", a_dictionary[key])
