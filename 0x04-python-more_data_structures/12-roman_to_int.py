#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numbers = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        }
    subtractive_notation = False
    result = 0
    if type(roman_string) is str:
        for idx, num in enumerate(roman_string):
            if idx and\
                    roman_numbers[num] > roman_numbers[roman_string[idx - 1]]:
                subtractive_notation = True
            if not subtractive_notation:
                result += roman_numbers[num]
            else:
                result += roman_numbers[num]
                result -= roman_numbers[roman_string[idx - 1]] * 2
            subtractive_notation = False
    return result
