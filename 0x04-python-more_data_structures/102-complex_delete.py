#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if type(a_dictionary) is dict:
        keys_to_del = []
        for k, v in a_dictionary.items():
            if v == value:
                keys_to_del.append(k)
        for key in keys_to_del:
            del a_dictionary[key]
    return a_dictionary
