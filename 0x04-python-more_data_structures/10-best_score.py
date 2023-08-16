#!/usr/bin/python3
def best_score(a_dictionary):
    m = {'value': -float('inf'), 'name': None}
    if type(a_dictionary) is dict:
        for key, value in a_dictionary.items():
            if value > m['value']:
                m['value'] = value
                m['name'] = key
    return m['name']
