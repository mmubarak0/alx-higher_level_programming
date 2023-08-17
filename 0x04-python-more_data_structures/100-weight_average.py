#!/usr/bin/python3
def weight_average(my_list=[]):
    result = 0.0
    numerator = 0.0
    denominator = 0.0
    if type(my_list) is list and len(my_list) > 0:
        for x, y in my_list:
            numerator += x * y
            denominator += y
        result = numerator / denominator
    return result
